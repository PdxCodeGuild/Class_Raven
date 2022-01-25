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


def find_todo(todos, todo_id):
    # loop through the todos list to find the todo with the given todo_id
    for todo_index, todo in enumerate(todos):
        if todo['id'] == todo_id:
            return (todo_index, todo)


JSON_DB = './static/todos.json'


@app.route('/')
def index():
    todos = load_data(JSON_DB)

    # filter todos into completed/not completed
    complete_todos = [todo for todo in todos if todo['completed']]
    incomplete_todos = [todo for todo in todos if not todo['completed']]

    return render_template('index.html', complete_todos=complete_todos, incomplete_todos=incomplete_todos)


@app.route('/create', methods=['GET', 'POST'])
def create_todo():
    # when arriving to the form page, render the template with the form
    if request.method == 'GET':
        return render_template('create.html')

    # when receiving user's form data for a new todo item,
    # process it and redirect to index page
    elif request.method == 'POST':

        # if the form text is blank, return to the template with an error message
        if not request.form['text']:
            return render_template('create.html', error="Text cannot be blank!")

        # load all todo items from the database
        todos = load_data(JSON_DB)

        # build new todo item dictionary
        new_todo = {
            'id': len(todos) + 1,
            'text': request.form['text'],
            'completed': False
        }

        todos.append(new_todo)

        save_data(JSON_DB, todos)

        return redirect(url_for('index'))


@app.route('/update/<int:todo_id>', methods=['GET', 'POST'])
def update_todo(todo_id):
    todos = load_data(JSON_DB)

    # unpack the tuple into two separate variables
    todo_index, todo = find_todo(todos, todo_id)

    if request.method == 'GET':
        return render_template('update.html', todo=todo)

    elif request.method == 'POST':
        # if the form text is blank, return to the template with an error message
        if not request.form['text']:
            return render_template('update.html', error="Text cannot be blank!", todo=todo)

        # update the text
        todo.update({
            'text': request.form['text']
        })

        save_data(JSON_DB, todos)

        return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    todos = load_data(JSON_DB)

    todo_index, todo = find_todo(todos, todo_id)

    todos.pop(todo_index-1)

    save_data(JSON_DB, todos)

    return redirect(url_for('index'))


@app.route('/toggle-complete/<int:todo_id>')
def toggle_complete(todo_id):
    # load all todo items from the database
    todos = load_data(JSON_DB)

    # loop through the todos list to find the todo with the given todo_id
    for todo_index in range(len(todos)):
        todo = todos[todo_index]

        if todo['id'] == todo_id:
            break

    # flip the completed value to its opposite
    todo.update({
        'completed': not todo['completed']
    })

    todos[todo_index] = todo

    save_data(JSON_DB, todos)

    return redirect(url_for('index'))
