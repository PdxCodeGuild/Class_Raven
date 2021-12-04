from flask import render_template, request, redirect, url_for
from pw_genny.models import Data
from pw_genny import app


@app.route("/", methods=["GET", "POST"])
def index():

    return render_template("index.html")


@app.route("/enter_pw", methods=["GET", "POST"])
def entry():

    return render_template("entry.html", bitty_bet=['q', 's', 'e', 'd', 'r', 'g', 'y', 'y', 'h', 'j'])


@app.route("/execute", methods=['GET', 'POST'])
def execute():
    """Execute the password generation"""

    return redirect(url_for("entry"))
