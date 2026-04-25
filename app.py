import os
from flask import session
from antigravity import Antigravity, render_template, redirect, request
from lib.youtube_parser import get_cached_videos, get_channel_metadata, clear_cache
from lib.db import get_profiles, save_profile, get_profile_by_id, delete_profile, update_profile

antigravity_app = Antigravity()
app = antigravity_app.app
app.secret_key = "industrial_black_secret_key" # Required for sessions

# Restricted terms based on profile category
CATEGORY_FILTERS = {
    "Criança": ["violência", "gore", "política", "noticiário", "guerra", "terror", "armas", "crime", "debate"],
    "Adolescente": ["gore", "terror extremo", "conteúdo sensível"],
    "Adulto": []
}

# Security Middleware (Add headers to all responses)
@app.after_request
def add_security_headers(response):
    csp = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com https://www.youtube.com https://s.ytimg.com; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com https://www.gstatic.com; "
        "font-src 'self' data: https://fonts.gstatic.com https://cdnjs.cloudflare.com; "
        "img-src 'self' data: https://*.youtube.com https://*.ytimg.com https://*.ggpht.com https://www.gstatic.com; "
        "frame-src https://www.youtube-nocookie.com; "
        "connect-src 'self';"
    )
    response.headers['Content-Security-Policy'] = csp
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

def get_active_profile():
    profile_id = session.get("profile_id")
    if profile_id:
        p = get_profile_by_id(profile_id)
        if p: return p
    # If no valid profile in session, clear it
    session.pop("profile_id", None)
    return None

def filter_videos_by_profile(videos, profile):
    if not profile:
        return videos
    category = profile.get("category", "Adulto")
    forbidden_terms = CATEGORY_FILTERS.get(category, [])
    if not forbidden_terms:
        return videos
    filtered = []
    for v in videos:
        text = (v["title"] + " " + v["channel"]).lower()
        if not any(term in text for term in forbidden_terms):
            filtered.append(v)
    return filtered

@app.route("/")
def index():
    profile = get_active_profile()
    if not profile:
        profiles = get_profiles()
        if not profiles:
            return redirect("/create-profile")
        session["profile_id"] = profiles[0]["id"]
        profile = profiles[0]

    channel_filter = request.args.get("channel", "").lower()
    videos = get_cached_videos()
    channels = get_channel_metadata()
    videos = filter_videos_by_profile(videos, profile)
    
    if channel_filter:
        videos = [v for v in videos if channel_filter in v["channel"].lower()]
    return render_template("index.html", videos=videos, channels=channels, profile=profile, request=request)

@app.route("/manage-profiles")
def manage_profiles():
    profiles = get_profiles()
    return render_template("manage_profiles.html", profiles=profiles)

@app.route("/delete-profile/<int:pid>", methods=["POST"])
def remove_profile(pid):
    delete_profile(pid)
    if session.get("profile_id") == pid:
        session.pop("profile_id", None)
    return redirect("/manage-profiles")

@app.route("/create-profile")
def create_profile_page():
    return render_template("create_profile.html")

@app.route("/save-profile", methods=["POST"])
def save_profile_route():
    name = request.form.get("name")
    age = int(request.form.get("age", 0))
    if name and age:
        pid, cat = save_profile(name, age)
        session["profile_id"] = pid
    return redirect("/")

@app.route("/switch-profile/<int:pid>")
def switch_profile(pid):
    session["profile_id"] = pid
    return redirect("/")

@app.route("/api/profiles")
def api_profiles():
    return {"profiles": get_profiles()}

@app.route("/api/videos")
def api_videos():
    profile = get_active_profile()
    channel_filter = request.args.get("channel", "").lower()
    videos = get_cached_videos()
    videos = filter_videos_by_profile(videos, profile)
    if channel_filter:
        videos = [v for v in videos if channel_filter in v["channel"].lower()]
    return render_template("video_list.html", videos=videos)

@app.route("/api/refresh", methods=["POST"])
def api_refresh():
    clear_cache()
    profile = get_active_profile()
    videos = get_cached_videos()
    videos = filter_videos_by_profile(videos, profile)
    return render_template("video_list.html", videos=videos)

@app.route("/channels")
def channels_list():
    profile = get_active_profile()
    channels = get_channel_metadata()
    return render_template("index.html", videos=[], channels=channels, profile=profile, request=request)

@app.route("/history")
def history_page():
    profile = get_active_profile()
    channels = get_channel_metadata()
    return render_template("index.html", videos=[], channels=channels, profile=profile, request=request)

@app.route("/library")
def library_page():
    profile = get_active_profile()
    channels = get_channel_metadata()
    return render_template("index.html", videos=[], channels=channels, profile=profile, request=request)

@app.route("/refresh", methods=["POST"])
def refresh():
    clear_cache()
    return redirect("/")

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' in request.files:
        file = request.files['file']
        filename = file.filename.lower()
        if filename.endswith('.xml'):
            file.save('subscription_manager.xml')
            if os.path.exists('subscriptions.csv'): os.remove('subscriptions.csv')
            clear_cache()
        elif filename.endswith('.csv'):
            file.save('subscriptions.csv')
            if os.path.exists('subscription_manager.xml'): os.remove('subscription_manager.xml')
            clear_cache()
    return redirect("/")

@app.route("/sobre-2016")
def sobre_2016():
    return render_template("sobre_2016.html")

# Create a handler for Vercel
app_handler = app

# Emergency static file server for Vercel
@app.route('/static/<path:path>')
def send_static(path):
    from flask import send_from_directory
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    print("INICIANDO SERVIDOR EM http://127.0.0.1:5005")
    app.run(port=5005)
