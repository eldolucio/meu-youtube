import xml.etree.ElementTree as ET
import feedparser
import concurrent.futures
import requests
import time
import re
import os
import csv
from urllib.parse import urlparse, parse_qs

# Simple in‑memory cache (TTL 10 min)
_cache = {"data": None, "ts": 0}
_channel_cache = {"data": None, "ts": 0}


def parse_subscriptions():
    """Parse the YouTube subscriptions safely from XML (legacy) or CSV (Google Takeout 2026)."""
    # Look for any CSV or XML file that might contain subscriptions
    files_to_check = ["subscription_manager.xml", "subscriptions.csv", "inscricoes.csv", "inscrições.csv"]
    
    # Priority check
    active_file = None
    for f in files_to_check:
        if os.path.exists(f):
            active_file = f
            break
            
    if not active_file:
        return []

    # XML logic
    if active_file.endswith(".xml"):
        try:
            tree = ET.parse(active_file)
            return [node.get('xmlUrl') for node in tree.findall('.//outline[@xmlUrl]')]
        except Exception as e:
            print(f"Error parsing XML: {e}")
            
    # CSV logic (Google Takeout - Multi-language support)
    if active_file.endswith(".csv"):
        urls = []
        try:
            with open(active_file, newline='', encoding='utf-8') as csvfile:
                # Handle possible Byte Order Mark (BOM)
                content = csvfile.read()
                if content.startswith('\ufeff'):
                    content = content[1:]
                csvfile.seek(0)
                
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # Support for multiple languages and cases
                    channel_id = (
                        row.get('Channel Id') or 
                        row.get('Channel ID') or 
                        row.get('ID do canal') or 
                        row.get('Id do canal') or
                        # Fallback: check first column if headers are weird
                        list(row.values())[0] if row.values() else None
                    )
                    
                    if channel_id and channel_id.startswith('UC'):
                        urls.append(f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}")
        except Exception as e:
            print(f"Error parsing CSV: {e}")
        return urls
        
    return []


def extract_video_id(url):
    """Extract the YouTube video ID safely."""
    if not url:
        return None
    try:
        parsed_url = urlparse(url)
        if parsed_url.hostname == 'youtu.be':
            return parsed_url.path[1:]
        if parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
            if parsed_url.path == '/watch':
                p = parse_qs(parsed_url.query)
                return p.get('v', [None])[0]
            if parsed_url.path.startswith('/embed/'):
                return parsed_url.path.split('/')[2]
            if parsed_url.path.startswith('/v/'):
                return parsed_url.path.split('/')[2]
            if parsed_url.path.startswith('/shorts/'):
                parts = parsed_url.path.split('/')
                if len(parts) >= 3:
                    return parts[2]
    except Exception:
        pass
    return None


def fetch_feed(url):
    """Download a single RSS feed safely."""
    if not url:
        return None
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return feedparser.parse(response.content)
    except Exception:
        pass
    return None


def is_short(entry):
    """Detect Shorts by looking for '#shorts' in the title or '/shorts/' in the link."""
    combined = (entry.get('title', '') + entry.get('link', '')).lower()
    return bool(re.search(r"(#shorts|/shorts/)", combined))


def get_cached_videos(ttl=600):
    """Return the list of videos with basic safety and caching."""
    now = time.time()
    if _cache["data"] is not None and (now - _cache["ts"] < ttl):
        return _cache["data"]

    urls = parse_subscriptions()
    if not urls:
        return []

    video_list = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        feeds = list(executor.map(fetch_feed, urls))

    for feed in filter(None, feeds):
        channel_name = feed.feed.get('title', 'Canal Desconhecido')
        for entry in feed.entries:
            if is_short(entry):
                continue
            
            video_id = extract_video_id(entry.link)
            thumbnail = ''
            if 'media_thumbnail' in entry and entry.media_thumbnail:
                thumbnail = entry.media_thumbnail[0].get('url', '')
            elif video_id:
                thumbnail = f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"
                
            published_str = entry.get('published', '')
            published_ts = 0
            if entry.get('published_parsed'):
                try:
                    published_ts = time.mktime(entry.published_parsed)
                except Exception:
                    published_ts = 0
            
            video_list.append({
                "title": entry.get('title', 'Sem título'),
                "link": entry.get('link', '#'),
                "video_id": video_id,
                "channel": channel_name,
                "thumbnail": thumbnail,
                "published_ts": published_ts,
                "published_str": published_str
            })

    video_list.sort(key=lambda x: x["published_ts"], reverse=True)
    
    _cache["data"] = video_list
    _cache["ts"] = now
    return video_list


def get_channel_metadata(ttl=3600):
    """Fetch metadata (name, icon, id) for all subscribed channels."""
    now = time.time()
    if _channel_cache["data"] is not None and (now - _channel_cache["ts"] < ttl):
        return _channel_cache["data"]

    urls = parse_subscriptions()
    if not urls:
        return []

    channels = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        feeds = list(executor.map(fetch_feed, urls))

    for feed in filter(None, feeds):
        channel_name = feed.feed.get('title', 'Canal Desconhecido')
        # YouTube RSS usually provides the channel icon here
        icon = feed.feed.get('image', {}).get('href', 'https://www.gstatic.com/youtube/img/branding/favicon/favicon_144x144.png')
        
        channels.append({
            "name": channel_name,
            "icon": icon,
            "id": feed.feed.get('yt_channelid', '')
        })

    # Sort channels by name alphabetically
    channels.sort(key=lambda x: x["name"].lower())
    
    _channel_cache["data"] = channels
    _channel_cache["ts"] = now
    return channels


def clear_cache():
    """Manually clear the video and channel cache."""
    _cache["data"] = None
    _cache["ts"] = 0
    _channel_cache["data"] = None
    _channel_cache["ts"] = 0
