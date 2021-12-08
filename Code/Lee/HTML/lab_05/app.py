from flask import Flask, render_template, request, redirect, url_for
import json

from flask.json import load
app = Flask(__name__)


def load_data(filename):
    with open(filename, 'r') as json_file:
        return json.loads(json_file.read())

def save_data(filename, data):
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(data, indent=2))
    return

def calculate_price(user_order):
    # Evaluate tortilla, rice, beans, protein, cheese, and sour cream
    '''"tortilla": "white", "wheat", "spinach", "corn"
    "rice": "white", "brown"
    "beans": "black", "pinto"
    "protein": "none", "carnitas", "chicken", "sofritas"
    "cheese": "AddCheese", 'False'
    "sour_cream": "AddSourCream", 'False'
    }'''
    price = 8
    if user_order['tortilla'] in ["spinach", "wheat"]:
        price += 1
    if user_order['rice'] == "brown":
        price += 1
    if user_order['protein'] in ["carnitas", "sofritas"]:
        price += 3
    elif user_order['protein'] == "none":
        price -= 1
    if user_order['cheese'] == "AddCheese":
        price += 1
    if user_order['sour_cream'] == "AddSourCream":
        price += 1
    return price

JSON_DB = './static/files/orders.json'

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_order():
    user_order = {
        'first_name' : request.form['firstName'],
        'last_name'  : request.form['lastName'],
        'email_address' : request.form['email'],
        'delivery_instructions' : request.form['deliveryInstructions'],
        'tortilla' : request.form['tortilla-select'],
        'rice' : request.form['rice-select'],
        'beans' : request.form['beans-select'],
        'protein' : request.form['protein-select'],
        'cheese' : 'False',
        'sour_cream' : 'False',
    }

    try: 
        user_order['cheese'] = request.form['other-cheese']
    except:
        KeyError

    try:
        user_order['sour_cream'] = request.form['other-sourCream']
    except:
        KeyError


    save_data(JSON_DB, user_order)

    return render_template('index.html', user_order='True')

@app.route('/clear')
def clear_json():
    memo = []
    save_data(JSON_DB, memo)
    return redirect(url_for('index'))

@app.route('/reciept')
def view_reciept():
    reciept = load_data(JSON_DB)
    price = calculate_price(reciept)
    user_info = reciept['first_name'].capitalize() + " " + reciept['last_name'].capitalize()
    email_address = reciept['email_address']
    delivery_instructions = reciept['delivery_instructions']
    tortilla = reciept['tortilla'].capitalize()
    rice = reciept['rice'].capitalize()
    beans = reciept['beans'].capitalize()
    protein = reciept['protein'].capitalize()
    cheese = reciept['cheese'].capitalize()
    sour_cream  = reciept['sour_cream'].capitalize()



    return render_template('reciept.html', user_info=user_info, email_address=email_address, delivery_instructions=delivery_instructions, tortilla=tortilla, rice=rice, beans=beans, protein=protein, cheese=cheese, sour_cream=sour_cream, price=price)

app.run(debug=True)