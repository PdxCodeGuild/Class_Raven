from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def load_data(filename):
    with open(filename, 'r') as json_file:
        return json.loads(json_file.read())

def save_data(filename, data):
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(data, indent=2))

    return



@app.route('/')
def index():
    # load articles from JSON file
    articles = load_data('./static/articles.json')

    return render_template('index.html', articles=articles)


@app.route('/create', methods=['GET', 'POST'])
def create_article():
    # if the request method is GET, load blank article form
    if request.method == "GET":
        return render_template('articles/new.html', article=None)
    
    # if the request method is POST, use the form data to create a new article
    elif request.method == "POST":
        articles = load_data('./static/articles.json')

        new_article = {
            'userId': 2,
            'id': len(articles) + 1,
            'title': request.form['title'],
            'body': request.form['body']
        }

        # add the new article to the list
        articles.insert(0, new_article)

        # update the json file
        save_data('./static/articles.json', articles)

        # redirect to the index page
        return redirect(url_for('index'))


@app.route('/delete/<int:article_id>')
def delete_article(article_id):
    # find the article to be deleted
    articles = load_data('./static/articles.json')

    new_articles = []
    for article in articles:
        if article['id'] != article_id:
            new_articles.append(article)

    save_data('./static/articles.json', new_articles)

    return redirect(url_for('index'))
