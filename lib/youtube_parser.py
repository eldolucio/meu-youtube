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


def parse_subscriptions():
    """Parse the YouTube subscriptions safely from XML (legacy) or CSV (Google Takeout 2026)."""
    # Try XML first
    if os.path.exists("subscription_manager.xml"):
        try:
            tree = ET.parse("subscription_manager.xml")
            return [node.get('xmlUrl') for node in tree.findall('.//outline[@xmlUrl]')]
        except Exception as e:
            print(f"Error parsing XML: {e}")
            
    # Try CSV (Google Takeout)
    if os.path.exists("subscriptions.csv"):
        urls = []
        try:
            with open("subscriptions.csv", newline='', encoding='utf-8') as csvfile:
                # Handle possible Byte Order Mark (BOM)
                content = csvfile.read()
                if content.startswith('\ufeff'):
                    content = content[1:]
                csvfile.seek(0)
                
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # Google Takeout CSV uses "Channel Id" or "Channel ID"
                    channel_id = row.get('Channel Id') or row.get('Channel ID')
                    if channel_id:
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
                return parsed_url.path.split('/')[2]
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

    # Sort by date (descending)
    video_list.sort(key=lambda x: x["published_ts"], reverse=True)
    
    _cache["data"] = video_list
    _cache["ts"] = now
    return video_list


def clear_cache():
    """Manually clear the video cache."""
    _cache["data"] = None
    _cache["ts"] = 0
