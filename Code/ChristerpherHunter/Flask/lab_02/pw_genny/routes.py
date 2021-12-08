from flask import render_template, request
from pw_genny import app
from random import sample, shuffle
from string import ascii_lowercase, ascii_uppercase, punctuation, digits


def password_genny(low_lets: int, up_lets: int, num_of_numbers: int, spec_chars: int) -> str:
    """Generate a password based on the user input"""

    pw_length = str(low_lets + up_lets + num_of_numbers + spec_chars)

    password = \
        sample(ascii_lowercase, low_lets) +\
        sample(ascii_uppercase, up_lets) +\
        sample(punctuation, spec_chars) +\
        sample(digits, num_of_numbers)

    shuffle(password)

    return "".join(password)


@app.route("/", methods=["GET", "POST"])
def index():

    return render_template("index.html")


@app.route("/show_pw", methods=["POST"])
def show_pw():
    """Execute the password generation"""

    p_word = password_genny(
        low_lets=int(request.form["lw-letters"]),
        up_lets=int(request.form["up-letters"]),
        num_of_numbers=int(request.form["num-nums"]),
        spec_chars=int(request.form["spec-chars"])
    )

    return render_template("show_page.html", p_word=p_word)


@app.route("/hash_pw/<int:pw_length>", methods=["POST"])
def hash_pw(pw_length):
    """Execute the password hashing"""

    hash_word = "dsf45sa6dgf4d6f5g749a864df5a6fd7a96s5"
    print(pw_length)

    words = str()
    with open("pw_genny/static/assets/words.txt") as word_list:
        words = " ".join(sample(word_list.read().split("\n"), pw_length))
    
    return render_template("hashed.html", hash_word=words)
