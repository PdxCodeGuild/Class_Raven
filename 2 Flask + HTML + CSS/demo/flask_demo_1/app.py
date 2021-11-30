from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():

    links = ["Home", "About", "Contact"]
    name = "Keegan"

    temperature = 55

    numbers = [11, 22, 33, 44, 55]

    context = {
        "name": name,
        "temperature": temperature,
        "numbers": numbers,
        "links": links,
    }

    # return render_template('index.html', name=name, temperature=temperature, numbers=numbers)
    return render_template('index.html', context=context)

@app.route('/about')
def about():
    return "We are a class learning Python!"

@app.route('/posts/<int:post_id>')
def post_detail(post_id):
    return f'Showing post number {post_id}'

@app.route('/users/<string:username>')
def user_profile(username):
    return f'Showing profile for {username}'

@app.route('/login')
def login():

    username = request.args['username']
    password = request.args['password']

    return f'Login attempt username: {username} password: {password}'

app.run(debug=True)