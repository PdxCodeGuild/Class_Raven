from flask import render_template, request, redirect, url_for
from pw_genny.models import Data
from pw_genny import app


@app.route("/")
def index():

    return render_template("index.html")
