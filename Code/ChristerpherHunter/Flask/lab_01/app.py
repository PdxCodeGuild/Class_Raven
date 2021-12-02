from flask import Flask, render_template, request, redirect, url_for
from json import dumps, loads, decoder

app = Flask(__name__)

db = "lab_01/db.json"


def load_data() -> dict():
    """Load the data to be excercised"""

    with open(db, "r") as f_read:
        return loads(f_read.read())


def clear_order() -> None:
    """Remove the data in the json db"""

    with open(db, "r+") as f_clear:
        f_clear.truncate(0)


def save_data(data: dict) -> None:
    """Save the data input from the user"""

    with open(db, "w") as f_write:
        f_write.write(dumps(data, indent=2))


@app.route("/")
def index():

    try:
        return render_template("index.html", orders=load_data())
    except decoder.JSONDecodeError:
        null_info = {"No Oders Placed": ""}
        return render_template("index.html", orders=null_info)


@app.route("/orders", methods=['POST', 'GET'])
def orders():

    if request.method == "POST":
        order_dict = {
            "First Name": request.form["f-name"].capitalize(),
            "Last Name": request.form["l-name"].capitalize(),
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


@app.route("/clear", methods=['POST'])
def reset_receipt():
    """"Clear the db when the clear button is pressed"""

    clear_order()

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
