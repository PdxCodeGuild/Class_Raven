from flask import Flask, request
from flask import render_template as render
from string import ascii_lowercase, ascii_uppercase, punctuation, digits


app = Flask(__name__)

@app.route('/')
def index():
  charsets = ['lower case', 'upper case', 'special characters', 'digits']
  return render('index.html', charsets=charsets)
