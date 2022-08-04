import os
import sys
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

print("Hello World", file=sys.stderr)

def create_app():
    return app

if __name__ == "__main__":
    # NOTE: this runs when app.py is called directly (cli or docker-compose.local/entrypoint.sh)
    # NOTE: if debug=True, reloader will run
    app.run(debug=True, host="0.0.0.0", port=5141)
else:
    # NOTE: this runs when app.py is imported, i.e. production scenario/Waitress to serve app
    create_app()
