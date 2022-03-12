from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def booyah():
    text= "rrrrrraaaah!!"
    return render_template('practice.html', text=text)
