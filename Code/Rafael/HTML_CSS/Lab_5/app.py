from flask import Flask, render_template, request
# used for API requests "import requests"

app = Flask(__name__)

@app.route('/')
def index():
    text = ''
    return render_template('index.html', text = text)




@app.route('/index', methods=['GET', 'POST'])
def receipt():
    text = '' 
    order = {
        'tortillas':request.form['tortillas'],
        'rice':request.form['rice'],
        'beans':request.form['beans'],
        'protein':request.form['protein'],
        #ImmutableMultiDict instead, getlist() to display multiple checkboxes in receipt.
        'additional':request.form.getlist('additional'),
        'instructions':request.form['instructions'],
        'firstname':request.form['firstname'],
        'lastname':request.form['lastname']
    }
    return render_template('receipt.html', order = order, text = text) 


app.run(debug=True)

"""
& env:FLASK_APP=app.py

$ export FLASK_APP=app.py 

export FLASK_ENV=development

$ python -m flask run

"""





