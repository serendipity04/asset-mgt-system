from flask import render_template, redirect, url_for, flash
from .. import db
from . import main

@main.route("/dashboard")
@main.route('/')
def index():
    flash("Welcome!", 'success')
    return render_template('index.html', user="david")

