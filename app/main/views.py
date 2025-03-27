from flask import render_template, redirect, url_for, current_app
from .. import db
from . import main

@main.route("/dashboard")
@main.route('/')
def index():
    return render_template('index.html')