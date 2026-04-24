import os
from antigravity import Antigravity, render_template, redirect, request
from lib.youtube_parser import get_cached_videos, clear_cache

app = Antigravity()

# Security Middleware (Add headers to all responses)
@app.app.after_request
def add_security_headers(response):
    # Content Security Policy: Only allow iframes from youtube-nocookie
    csp = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com; "
        "font-src 'self' https://fonts.gstatic.com; "
        "img-src 'self' data: https://*.youtube.com https://*.ytimg.com; "
        "frame-src https://www.youtube-nocookie.com; "
        "connect-src 'self';"
    )
    response.headers['Content-Security-Policy'] = csp
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

@app.route("/")
def index():
    channel_filter = request.args.get("channel", "").lower()
    videos = get_cached_videos()
    if channel_filter:
        videos = [v for v in videos if channel_filter in v["channel"].lower()]
    # Serving template index.html (standardized from index_v2.html)
    return render_template("index.html", videos=videos, request=request)

@app.route("/api/videos")
def api_videos():
    channel_filter = request.args.get("channel", "").lower()
    videos = get_cached_videos()
    if channel_filter:
        videos = [v for v in videos if channel_filter in v["channel"].lower()]
    return render_template("index.html", videos=videos, request=request)

@app.route("/channels")
def channels_list():
    return render_template("index.html", videos=[], request=request)

@app.route("/history")
def history_page():
    return render_template("index.html", videos=[], request=request)

@app.route("/library")
def library_page():
    return render_template("index.html", videos=[], request=request)

@app.route("/refresh", methods=["POST"])
def refresh():
    clear_cache()
    return redirect("/")

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' in request.files:
        file = request.files['file']
        if file.filename.endswith('.xml'):
            # Security: Ensure filename is safe or use a fixed name
            file.save('subscription_manager.xml')
            clear_cache()
    return redirect("/")

@app.route("/sobre-2016")
def sobre_2016():
    return render_template("sobre_2016.html")

# Create a handler for Vercel
app_handler = app.app

if __name__ == "__main__":
    app.run(port=8000)
