import os
from flask import Flask, render_template as _render_template, request as _request, redirect as _redirect

class Antigravity:
    def __init__(self):
        # Use absolute paths relative to the project root (one level up from this file)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        static_path = os.path.join(base_dir, 'static')
        template_path = os.path.join(base_dir, 'templates')
        self.app = Flask(__name__, static_folder=static_path, template_folder=template_path)

    def __call__(self, environ, start_response):
        return self.app(environ, start_response)

    def route(self, rule, methods=None):
        # Proxy Flask's route decorator
        return self.app.route(rule, methods=methods)

    def run(self, host='0.0.0.0', port=8000):
        # Run the Flask development server
        self.app.run(host=host, port=port)

    # expose Flask helpers
    @property
    def request(self):
        return _request

    def render_template(self, template_name, **context):
        return _render_template(template_name, **context)

# expose Flask helpers at module level for direct import
render_template = _render_template
redirect = _redirect
request = _request



# expose a convenient import name similar to the original Antigravity package
__all__ = ['Antigravity']
