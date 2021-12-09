from flask import Flask, render_template, request, url_for
import string

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/rot_show', methods=['GET', 'POST'])
def show_rotation():
    # creates a list with what i pass into the list function
    if not request.form['query']:
        return render_template('index.html', error="Text cannot be blank!")
    # here we have list of the alphabet
    if not request.form['rotation']:
        return render_template('index.html', error="Text cannot be blank!")
    
    uppercase_alphabet = list(string.ascii_uppercase)
    query = request.form.get('query')
    rotation = request.form.get('rotation')
    rotation = int(rotation)
    encrypt = list(query.upper())
    
    # I want to compare each index of encrypt with the uppercase_alphabet index

    encrypted_message = []

    index = 0

    # i want to loop through the list for as many characters are in list,
    for index in range(len(encrypt)):
        # its only doing first index during the loop
        # for encrypt[index] in uppercase_alphabet[index]:

        # this code is appending to the encrypt list
        # this is just changing the uppercase alphabet list
        cipher = uppercase_alphabet.index(encrypt[index])
        encrypted_message.append(uppercase_alphabet[(cipher + rotation) % 26])

        index += 1

    return render_template("rot_show.html", uppercase_alphabet=uppercase_alphabet, encrypt=encrypt, encrypted_message=encrypted_message)
