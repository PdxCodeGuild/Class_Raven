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

JSON_DB = "./static/JSON_DB.json"


# @app.route('/')
# def index():

#     return render_template('index.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    else:

        user = request.form["fname"]
        user2 = request.form["lname"]
        return f'Welcome! {user} {user2}' 
        


@app.route('/', methods=["POST", "GET"])
def food_order():
    if request.method == "GET":
        categories =  ['tortilla', 'rice', 'bean', 'protein', 'additional_ingredients' ]
        options = {
            'tortilla': ['White Flour', 'Wheat Flour', 'Spinach', 'Corn'],
            'rice' : ['White Rice', 'Brown Rice'],
            'bean': ['Black Beans', 'Pinto Beans'],
            'protein' : ['Carnitas', 'Chicken', 'Sofritas', 'None'],
            
        }
        images = ['tortila', 'rice', 'bean', 'protein']

        extras = {
            "extra":['cheese', 'sour cream']
        }


        return render_template("index.html", options=options, categories=categories, images=images, extras=extras)

    elif request.method == "POST":
        
        return render_template("receipt.html")


@app.route('/receipt', methods=["POST", "GET"])

def receipt():
    if request.method == "GET":
        
        return render_template()

    elif  request.method == "POST":
       
        cost = {
            'tortilla': 2,
            'rice': 3,
            'bean': 1,
            'protein' : 3,
            'extras': .5,
            'none': 0
        } 


        print(request.form)
        
        burrito = {
            'tortilla': request.form['tortilla'],
            'rice': request.form['rice'],
            'bean': request.form['bean'],
            'protein': request.form['protein'],
            'extras': request.form['extras'],    
            'delivery_instructions': request.form['delivery_instructions']
        }
        
        
        save_data(JSON_DB, burrito)
        
        total = 0
        
            
      
        
        return render_template("receipt.html", burrito=burrito, total=total, cost=cost) 


if __name__ == "__main__":
    app.run(debug=True)
