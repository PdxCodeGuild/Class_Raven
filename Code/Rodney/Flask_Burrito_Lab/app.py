from logging import debug
from flask import Flask, render_template
from flask import request
import json

app = Flask(__name__)

# def load_data(filename):
#     with open(filename, 'r') as json_file:
#         return json.loads(json_file.read())

# def load_data(filename, data):
#     with open(filename, 'w') as json_file:
#         json_file.write(json.dumps(data, indent=2))
    # return 

@app.route('/')
def index():
    
    return render_template('index.html')
    

@app.route('/receipt', methods=["POST"])
def receipt():
    
    receipt_dict = {
    'first':request.form['first'],
    'last':request.form['last'],
    'beans':request.form['beans'],
    'tortilla':request.form['tortilla'],
    'rice':request.form['rice'],
    'protein':request.form['protein'],
    'instructions':request.form['instructions'],
    'additional':request.form.getlist('additional'),
    'how-many': (int(request.form['how-many']))
    }

    return render_template('receipt.html', receipt_dict=receipt_dict)




app.run(debug=True)







# @app.route('/about')
# def about():
#     return "My name is Rodney"

# @app.route("/posts/<int:post_id>")
# def post_detail(post_id):
#     return f"showing post number {post_id}"

# @app.route("/user/<string:username>")
# def user_profile(username):
#     return f"Wecome {username}" 

# @app.route("/login")
# def login():
#     username = request.args['username']
#     password = request.args['password']

#     return f"login attempt username: {username} password {password}"
