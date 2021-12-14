from logging import debug
from flask import Flask, render_template
from flask import request
import random
import string
from string import ascii_letters, ascii_lowercase, ascii_uppercase, punctuation


app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template('index.html')
    

@app.route('/password', methods=["POST"])
def password():
    
    numbers = int(request.form['how-many1'])
    letters = int(request.form['how-many2'])
    user_punctuation = int(request.form['how-many3'])

    ascii_letters = string.ascii_letters
    digits = string.digits
    puncuation = string.punctuation

    possibile_letters = ascii_letters
    possible_numbers = digits
    possible_punct = punctuation

    y = 1
    password_numbers = ""
    while y <= numbers:
        password_numbers += random.choice(possible_numbers)
        y += 1

    x = 1               
    password_letters = ""   
    while x <= letters:
        password_letters += random.choice(possibile_letters)
        x += 1 

    z = 1
    password_punct = ""
    while z <= user_punctuation:
        password_punct += random.choice(possible_punct)
        z += 1 

    user_password = str(password_letters + password_numbers + password_punct) 

    final_password = list(user_password) 

    random.shuffle(final_password)  


    return render_template('password.html', final_password=final_password)



app.run(debug=True)


