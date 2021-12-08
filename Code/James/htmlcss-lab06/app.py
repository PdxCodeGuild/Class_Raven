from flask import Flask, render_template, request, redirect, url_for 
import json
import string

app = Flask(__name__)

@app.route('/')
def hello_world():
    print(hello_world)
    return 'HELLO, WORLD!'


@app.route('/rot_show')
def show_rotation():
    
    encrypt = list('catdog')
    
    
    uppercase_alphabet = list(string.ascii_uppercase)

    if encrypt in uppercase_alphabet:
        encrypt += 13
    
    
    
    return render_template("rot_show.html", uppercase_alphabet= uppercase_alphabet, encrypt=encrypt)

    