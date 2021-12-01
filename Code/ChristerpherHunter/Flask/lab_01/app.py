from flask import Flask, render_template, request, redirect, url_for
from json import dumps, loads

app = Flask(__name__)


def load_data() -> dict():
    """Load the data to be excercised"""

    with open("lab_01/db.json", "r") as f_read:
        return loads(f_read.read())


def save_data(data: dict) -> None:
    """Save the data input from the user"""

    with open("lab_01/db.json", "w") as f_write:
        f_write.write(dumps(data, indent=2))


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/orders", methods=['POST', 'GET'])
def orders():

    if request.method == "POST":
        order_dict = {
            "first_name": request.form["f-name"].lower(),
            "last_name": request.form["l-name"].lower(),
            "tortilla": request.form["tortilla-type"].lower(),
            "rice": request.form["rice"].lower(),
            "beans": request.form["beans"].lower(),
            "protein": request.form["protein"].lower(),
            "additional_ingredients": request.form.getlist("add-ingr"),
            "delivery_instructions": request.form["deliv-instr"].lower(),
        }

    save_data(order_dict)
    # print(load_data())

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
