from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')




@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method =="GET":  
        return render_template("login.html")
         

    else: 
        
        user = request.form["fname"]
        user2 = request.form["lname"]
        return f'Welcome! {user} {user2}'


@app.route('/order', methods=["POST", "GET"])
def food_order():
    if request.method == "POST":
        meat = request.form['name']
        return f'<h1> You ordered {meat} </h1>'
    else:
        meat_options = ['Carnitas', 'Chicken', 'Sofritas', 'None' ]
        return render_template("order.html", meat_options = meat_options)
        

# @app.route("/<usr>")
# def user(usr, usr2):
#     return f"<h1>Hello! {usr} {usr2} </h1>"

    


if __name__ == "__main__":
    app.run(debug=True)
