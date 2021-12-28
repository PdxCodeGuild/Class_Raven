from flask import Flask, jsonify, request, render_template
import json

from flask.json import load

# jsonify converts data to json and wraps it in an HTTP Response object

app = Flask(__name__)


# Database helpers

def load_data(filename):
    '''Load the data from the "database" from the filename'''
    with open(filename, 'r') as json_file:
        return json.loads(json_file.read())


def save_data(filename, data):
    '''Save the data to the "database" from the filename'''
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(data, indent=2))

    return


def find_todo(todos, todo_id):
    '''return the todo with the given todo_id'''
    for todo in todos:
        if todo['id'] == todo_id:
            return todo


JSON_DB = './static/todos.json'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/todos')
def get_todos():
    # create blank dict for response data
    response_data = {}

    # get all the todo items from the "database"
    todos = load_data(JSON_DB)

    # separate the todos based on completeness
    # incomplete_todos = [todo for todo in todos if not todo['complete']]
    # complete_todos = [todo for todo in todos if todo['complete']]

    # for loop version of line 46
    # incomplete_todos = []
    # for todo in todos:
    #     if not todo['complete']:
    #         incomplete_todos.append(todo)

    response_data = {
        'statusCode': 200,
        'todos': todos
    }

    return jsonify(response_data)


@app.route('/todos/create', methods=['POST'])
def create_todo():
    # create empty response dict
    response_data = {}

    form_data = request.get_json()

    # get the new todo text from the request
    text = form_data.get('text')

    # if no text was passed with the request, return an error
    if not text:
        # provide an error message in the response data
        response_data = {
            'statusCode': 400,
            'error': 'Text cannot be blank!'
        }
    else:
        # load all the todo items from the "database"
        todos = load_data(JSON_DB)

        # calculate the id number for the new todo item
        if not todos:
            todo_id = 1
        else:
            # new todo has id of 1 more than the last todo item
            todo_id = todos[-1]['id'] + 1

        # build the new todo item dict
        new_todo = {
            'id': todo_id,
            'text': text,
            'complete': False
        }

        # add the todo to the list
        todos.append(new_todo)

        # save the todos to the "DB"
        save_data(JSON_DB, todos)

        response_data = {
            'statusCode': 200,
            'message': 'Created successfully!',
            'todos': todos
        }

    return jsonify(response_data)


@app.route('/todos/update', methods=['POST'])
def update_todo():
    response_data = {}

    # get the data from the POST request
    form_data = request.get_json()

    # get the new todo text and todoId from the request
    updated_text = form_data.get('text')
    todo_id = form_data.get('todoId')

    # if there is no todoId specified
    if not todo_id:
        response_data = {
            'statusCode': 400,
            'error': 'Item not found!'
        }
    # if the text is blank
    elif not updated_text:
        response_data = {
            'statusCode': 400,
            'error': 'Text cannot be blank!'
        }

    # update the todo
    else:
        # get all todos
        todos = load_data(JSON_DB)

        # find the todo with the given id
        todo = find_todo(todos, todo_id)

        # if no todo item exists with the given id, return an error
        if not todo:
            response_data = {
                'statusCode': 400,
                'error': 'Item not found!'
            }
        else:
            # update the text
            todo.update({
                'text': updated_text
            })

            # save the todos to the DB
            save_data(JSON_DB, todos)

            # set successful response data
            response_data = {
                'statusCode': 200,
                'message': 'Updated successfully!',
                'todos': todos
            }

    return jsonify(response_data)


@app.route('/todos/delete', methods=['POST'])
def delete_todo():
    response_data = {}

    # get the data from the POST request
    form_data = request.get_json()

    # get the new todo text and todoId from the request
    todo_id = form_data.get('todoId')

# convert id to integer
    todo_id = int(todo_id)

    # if there is no todoId specified
    if not todo_id:
        response_data = {
            'statusCode': 400,
            'error': 'Item not found!'
        }

    else:
        # get all todos
        todos = load_data(JSON_DB)

        # find the todo with the given id
        todo = find_todo(todos, todo_id)

        # if no todo item exists with the given id, return an error
        if not todo:
            response_data = {
                'statusCode': 400,
                'error': 'Item not found!'
            }
        else:

            # delete the todo
            todos.remove(todo)

            # save the todos to the DB
            save_data(JSON_DB, todos)

            # set successful response data
            response_data = {
                'statusCode': 200,
                'message': 'Deleted successfully!',
                'todos': todos
            }

    return jsonify(response_data)


@app.route('/todos/toggle-complete', methods=['POST'])
def toggle_complete():
    response_data = {}

    # get the data from the POST request
    form_data = request.get_json()

    # get the new todo text and todoId from the request
    todo_id = form_data.get('todoId')

    # convert id to integer
    todo_id = int(todo_id)

    # if there is no todoId specified
    if not todo_id:
        response_data = {
            'statusCode': 400,
            'error': 'Item not found!'
        }

    else:
        # get all todos
        todos = load_data(JSON_DB)

        # find the todo with the given id
        todo = find_todo(todos, todo_id)

        # if no todo item exists with the given id, return an error
        if not todo:
            response_data = {
                'statusCode': 400,
                'error': 'Item not found!'
            }
        else:

            # delete the todo
            todo.update({
                'complete': not todo['complete']
            })

            # save the todos to the DB
            save_data(JSON_DB, todos)

            # set successful response data
            response_data = {
                'statusCode': 200,
                'message': 'Deleted successfully!',
                'todos': todos
            }

    return jsonify(response_data)
