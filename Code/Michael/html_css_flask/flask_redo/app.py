from flask import Flask, render_template, request, redirect, url_for
import sys
import os

sys.path.append(os.path.abspath("../.."))
import Python.rot13 as rot13

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/input", methods=["GET", "POST"])
def input():
    if request.method == "POST":
        text = request.form["text"]
        rotations = int(request.form["rotations"])
        rot = rot13.rot_cipher(text, rotations)
        return redirect(url_for("output", rot=rot))
    else:
        return render_template("input.html")


@app.route("/output/<rot>")
def output(rot):
    return render_template("output.html", rot=rot)
