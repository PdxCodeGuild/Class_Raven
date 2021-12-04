#redoing the password generator lab with flask and html/css

from flask import Flask, app, render_template, request, url_for
from random import choice
from string import ascii_lowercase,ascii_uppercase,digits,punctuation
app = Flask(__name__)





@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)