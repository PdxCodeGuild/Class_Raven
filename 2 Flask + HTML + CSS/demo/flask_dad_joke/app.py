from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/joke', methods=['GET', 'POST'])
def display_joke():

    headers = {
        "Accept": "application/json"
    }

    if request.method == 'GET':
        url = 'https://icanhazdadjoke.com/'
        response = requests.get(url, headers=headers)
        
        joke = response.json()['joke']
        
        # create a single-item list with the joke
        jokes = [joke]

    elif request.method == 'POST':
        query = request.form.get('query')
        url = f'https://icanhazdadjoke.com/search?term={query}'
        
        response = requests.get(url, headers=headers)

        results = response.json()['results']

        # pull the joke out of each dictionary
        jokes = [result['joke'] for result in results]

    return render_template('joke.html', jokes=jokes)








    

    # # if the query exists
    # if query:
    #     url += f'search?term={query}'

    


    # joke = response.json()['joke']

    # return render_template('joke.html', joke=joke)