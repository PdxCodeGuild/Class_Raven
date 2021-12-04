from flask import render_template, request, redirect, url_for
from pw_genny.models import Data
from pw_genny import app, db, bcrypt


def password_genny(low_lets: int, up_lets: int, num_of_numbers: int, spec_chars: int) -> str:
    """Generate a password based on the user input"""

    pw_length = str(low_lets + up_lets + num_of_numbers + spec_chars)

    return f"Password Length: {pw_length}"

@app.route("/", methods=["GET", "POST"])
def index():

    return render_template("index.html")


@app.route("/show_pw", methods=["POST"])
def show_pw():
    """Execute the password generation"""

    num_of_lowercase_letters = int(request.form["lw-letters"])
    num_of_capital_letters = int(request.form["up-letters"])
    num_of_numbers = int(request.form["num-nums"])
    num_of_special_characters = int(request.form["spec-chars"])

    p_word = password_genny(
        low_lets=num_of_lowercase_letters,
        up_lets=num_of_capital_letters,
        num_of_numbers=num_of_numbers,
        spec_chars=num_of_special_characters
    )

    return render_template("show_page.html", p_word=p_word)
