from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index1():
    
    return render_template('index.html')

@app.route('/login')
def login():
    # if request.method == 'POST':
    #    print("we posted")
    return render_template('login.html')



app.run(debug=True)
