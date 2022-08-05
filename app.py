import os
import sys
from flask import Flask, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from config import host, port, database, user, password

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@{host}/{database}"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:b61a657a49bded402e7b973876160162a77aa8ce004557a926dbc12778209d84@localhost/d4kpadureecp54"
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Event: {self.description}"

    def __init__(self, description, first_name, last_name):
        self.description = description
        self.first_name = first_name
        self.last_name = last_name


@app.route('/')
def home():
    return "Hey this is the home page"

def create_app():
    return app

if __name__ == "__main__":
    # NOTE: this runs when app.py is called directly (cli or docker-compose.local/entrypoint.sh)
    # NOTE: if debug=True, reloader will run
    app.run(debug=True, host="0.0.0.0", port=5141)
else:
    # NOTE: this runs when app.py is imported, i.e. production scenario/Waitress to serve app
    create_app()
