import string 
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def lock():

    abc = string.ascii_lowercase    # abcdefghijklmnopqrstuvwxyz
    new_string = ""  

    word = request.form['word']
    word = word.lower()
    rotations = request.form['rotations']
    rotations = int(rotations)

    for character in word:
        if character in abc:
            new_string += abc[(abc.find(character) + rotations) % 26]
        else:
            new_string += character    # This catches spaces that are entered



    user_input = {
        'word': new_string,
        'rotations': rotations
    }


    return render_template('result.html', word=user_input['word'])

app.run(debug = True) 