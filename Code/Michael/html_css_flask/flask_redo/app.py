from flask import Flask, render_template, request, redirect, url_for
import sys
import os
sys.path.append(os.path.abspath("../.."))
import Python.rot13 as rot13

app = Flask(__name__)

@app.route('/')
def index():
    ...
    
@app.route('/input', methods=['GET','POST'])
def input():
    ...
    
@app.route('/output', methods=['GET','POST'])
def output():
    ...