from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todo_app.models import TodoItem

from .serializers import TodoSerializer


def index(request):
    return render(request, 'index.html')


@api_view(['GET'])
def todo_list(request):
    response = Response()

    todos = TodoItem.objects.all()

    # many=True will allow serialization of multiple objects
    todo_serializer = TodoSerializer(todos, many=True)

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