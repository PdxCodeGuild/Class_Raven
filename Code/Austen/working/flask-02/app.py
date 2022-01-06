from flask import Flask, request
from flask import render_template as render
from string import ascii_lowercase, ascii_uppercase, punctuation, digits
from random import randint


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    charsets = ['lower case', 'upper case', 'special characters', 'digits']
    strings = {'lower case': ascii_lowercase, 'upper case': ascii_uppercase, 'special characters': punctuation, 'digits': digits}
    if request.method == 'POST':
        charsets = request.form
        charset = []
        password = []
        for key in charsets.keys():
            count = int(charsets[key])
            if count > 0:
                set = strings[key]
                for i in range(count):
                    index = randint(0, len(set) - 1)
                    char = set[index]
                    charset.append(char)
        while len(charset) > 0:
            index = randint(0, len(charset) - 1)
            char = charset.pop(index)
            password.append(char)
        password = ''.join(password)



        return render('password.html', charset=charset, password=password)
    return render('index.html', charsets=charsets)
