from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo_app.models import TodoItem

from .serializers import TodoSerializer


def index(request):
    return render(request, 'index.html')

# the @api_view decorator tells DRF that this view
# will return JSON instead of a standard Django HTTP Response
@api_view(['GET'])
def todo_list(request):
    # create empty response object
    response = Response()

    # get all the todo items from the database
    todos = TodoItem.objects.all()

    # many=True will allow serialization of multiple objects
    todo_serializer = TodoSerializer(todos, many=True)

    # attach the serialized data to the response object
    response.data = {
        'todos': todo_serializer.data
    }

    return response


@api_view(['POST'])
def create_todo(request):
    # create empty response object
    response = Response()

    # extract the new todo text from the request data
    new_todo_text = request.data.get('new_todo_text')

    # instanciate a TodoSerialier with the text from the request
    todo_serializer = TodoSerializer(data={'text': new_todo_text})

    # if all serializer fields are valid
    if todo_serializer.is_valid():
        # create a new TodoItem object
        todo_serializer.save()

        # get all todos from the database
        todos = TodoItem.objects.all()

        # many=True will allow serialization of multiple objects
        todo_serializer = TodoSerializer(todos, many=True)

        # attach todo data to the response object
        response.data = {
            'todos': todo_serializer.data
        }
    

    return response

@api_view(['POST'])
def toggle_complete(request, todo_id):
    # create empty response object
    response = Response()

    # find the item or raise 404
    todo = get_object_or_404(TodoItem, id=todo_id)

    # flip the complete value
    todo.complete = not todo.complete
    todo.save()

    # get all todos from the database
    todos = TodoItem.objects.all()

    # many=True will allow serialization of multiple objects
    todo_serializer = TodoSerializer(todos, many=True)

    # attach todo data to the response object
    response.data = {
        'todos': todo_serializer.data
    }

    return response


@api_view(['POST'])
def delete_todo(request, todo_id):
    # create an empty response object
    response = Response()

    # find the item or raise 404
    todo = get_object_or_404(TodoItem, id=todo_id)

    # delete the todo
    todo.delete()

    # get all todos from the database
    todos = TodoItem.objects.all()

    # many=True will allow serialization of multiple objects
    todo_serializer = TodoSerializer(todos, many=True)

    # attach todo data to the response object
    response.data = {
        'todos': todo_serializer.data
    }

    return response

