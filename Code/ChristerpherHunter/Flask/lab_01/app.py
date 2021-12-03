from flask import Flask, render_template, request, redirect, url_for
from json import dumps, loads, decoder
from jinja2 import exceptions

app = Flask(__name__)

db = "lab_01/db.json"


def load_data() -> dict():
    """Load the data to be excercised"""

    with open(db, "r") as f_read:
        return loads(f_read.read())


def save_data(data: dict) -> None:
    """Save the data input from the user"""

    with open(db, "w") as f_write:
        f_write.write(dumps(data, indent=2))


@app.route("/")
def index() -> object:

    # try:
    return render_template("index.html")
    # except (IndexError, exceptions.UndefinedError):
    #     null_info = {"No Oders Placed": ""}
    #     return render_template("index.html", orders=null_info, metadata=None)


@app.route("/orders", methods=['POST'])
def orders() -> object:

    data_list = load_data()

    order_dict = {
        "First Name": request.form["f-name"].capitalize(),
        "Last Name": request.form["l-name"].capitalize(),
        "Tortilla": request.form["tortilla-type"].capitalize(),
        "Rice": request.form["rice"].capitalize(),
        "Beans": request.form["beans"].capitalize(),
        "Protein": request.form["protein"].capitalize(),
        # Pretty print the list
        "Additional Ingredients": ", ".join(map(str, request.form.getlist("add-ingr"))),
        "Delivery Instructions": request.form["deliv-instr"].lower(),
    }
    order_metadata = {
        "id": len(data_list),
        "confirmed": False,
        "order filled": False
    }

    data = {
        "metadata": order_metadata,
        "order": order_dict
    }

    data_list.append(data)
    save_data(data_list)

    # return redirect(url_for('index', orders=orders, metadata=None))
    return render_template('index.html', orders=load_data()[-1]["order"], metadata=None)


@app.route("/clear", methods=['POST'])
def reset_receipt() -> object:
    """"Clear the db when the clear button is pressed"""

    null_info = {"Form Cleared": ""}

    return render_template('index.html', orders=null_info, metadata=None)
    # return redirect(url_for("index", orders=null_info))


@app.route("/confirmation", methods=['GET', 'POST'])
def order_confirm() -> object:
    """Confirm the order placed is correct"""

    data_list = load_data()
    data_list[-1]["metadata"].update({
        'confirmed': True
    })

    save_data(data_list)

    return render_template('confirmation.html', orders=load_data()[-1]["order"], metadata=None)


if __name__ == "__main__":
    app.run(debug=True)
