from flask import Flask, render_template, request, redirect, url_for
import json
app = Flask(__name__)

def load_data(filename):
    with open(filename, 'r') as json_file:
        return json.loads(json_file.read())

def save_data(filename, data):
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(data, indent=2))

    return

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    else:

        user = request.form["fname"]
        user2 = request.form["lname"]
        return f'Welcome! {user} {user2}' 
        


@app.route('/order', methods=["POST", "GET"])
def food_order():
    if request.method == "GET":
        categories =  ['tortilla', 'rice', 'bean', 'protein', 'additional_ingredients' ]
        options = {
            'tortilla': ['White Flour', 'Wheat Flour', 'Spinach', 'Corn'],
            'rice' : ['White Rice', 'Brown Rice'],
            'bean': ['Black Beans', 'Pinto Beans'],
            'protein' : ['Carnitas', 'Chicken', 'Sofritas', 'None'],
            'additional_ingredients' : ['Cheese', 'Sour Cream']
        }
        images = ['tortila', 'rice', 'bean', 'protein', 'additional_ingredients']




        return render_template("order.html", options=options, categories=categories, images=images)

    elif request.method == "POST":
        
        return render_template("receipt.html")


@app.route('/receipt', methods=["POST", "GET"])

def receipt():
    if request.method == "GET":
        
        return f'wlkefjaldkjflakdj'

    elif  request.method == "POST":
          cost = {
            'tortilla': 2,
            'rice': 3,
            'bean': 1,
            'protein' : 3,
            'additional_ingredients': .5
        } 
        
        return render_template("receipt.html") 


if __name__ == "__main__":
    app.run(debug=True)
