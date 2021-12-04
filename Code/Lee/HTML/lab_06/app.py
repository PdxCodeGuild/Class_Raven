from flask import Flask, render_template, request, redirect, url_for
import json, string

from flask.json import load
app = Flask(__name__)

def load_data(filename):
    with open(filename, 'r') as json_file:
        return json.loads(json_file.read())

def save_data(filename, data):
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(data, indent=2))

    return

JSON_DB = './static/memo.json'
    
@app.route('/')
def index():
    memo = load_data(JSON_DB)

    return render_template('index.html', memo=memo)

@app.route('/encode', methods=['POST'])
def encode_message():
    user_string = request.form['raw_string']
    rot = int(request.form['raw_rot'])
    alphabet_printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-.:;<=>?@[]^_`{|}~' + ' ' # 91 
    shifted_alphabet_printable = alphabet_printable[len(alphabet_printable)-rot:] + alphabet_printable[0:(len(alphabet_printable)-rot)] # rotates string to correspond with printable alphabet
    encrypted_message = ""
    memo = load_data(JSON_DB)

    for i in range(len(user_string)):
        encrypted_index = alphabet_printable.find(user_string[i])
        if encrypted_index == -1:
            encrypted_message += user_string[i]
        else:
            encrypted_message += shifted_alphabet_printable[encrypted_index]

    new_message = {
    'user_string': user_string,
    'rot': rot,
    'encrypted_message': encrypted_message
    }

    memo.append(new_message)
    save_data(JSON_DB, memo)

    return redirect(url_for('index'))
    
@app.route('/clear')
def clear_json():
    memo = []
    save_data(JSON_DB, memo)
    return redirect(url_for('index'))

app.run(debug=True)