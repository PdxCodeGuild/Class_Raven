from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')




@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method =="POST":
        user = request.form["fname"]
        user2 = request.form["lname"]
        return f'Showing profile for {user} {user2}'

    else:
        return render_template("login.html")


@app.route('/order', methods=["POST", "GET"])
def food_order():
    if request.method == "POST":
        meat = request.form['name']
        return f'<h1> You ordered </h1>'
    else:
        return render_template("order.html")


# @app.route("/<usr>")
# def user(usr, usr2):
#     return f"<h1>Hello! {usr} {usr2} </h1>"

    



@app.route('/order')
def order():
    print("here's your order")
    return render_template('order.html')

if __name__ == "__main__":
    app.run(debug=True)
