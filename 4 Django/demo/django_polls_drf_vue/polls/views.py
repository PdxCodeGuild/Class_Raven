from django.shortcuts import (
    render, # helps render html templates
    get_object_or_404, # returns the desired object if it exists or raises a 404 error
    reverse, # lookup the path associated with a view name
)
from django.http import HttpResponse, HttpResponseRedirect ,Http404


from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (
    QuestionDetailSerializer,
    ChoiceSerializer
)

# import the models from the Polls app
from .models import Question, Choice

from users.models import CustomUser

def index(request):
    return render(request, 'polls/index.html')


@api_view(['GET'])
def polls_list(request):
    # create blank JSON response
    response = Response()

    questions = Question.objects.all().order_by('-pub_date')

    # many=True allows multiple instances to be serialized
    question_serializer = QuestionDetailSerializer(questions, many=True)

    response.data = {
        'questions': question_serializer.data
    }

    return response
    
@api_view(['POST'])
def vote(request):
    response = Response()

    # the fetch request's body data is in request.data
    choice_id = request.data.get('choiceId')

    choice = get_object_or_404(Choice, id=choice_id)

    # increase the choice's vote count
    choice.votes += 1

    # save the updates
    choice.save()

    questions = Question.objects.all().order_by('-pub_date')

    # many=True allows multiple instances to be serialized
    question_serializer = QuestionDetailSerializer(questions, many=True)

    response.data = {
        'questions': question_serializer.data
    }

    return response


@api_view(['POST'])
def create_question(request):
    response = Response()

    # grab the values from the request data
    new_question_text = request.data.get('newQuestionText')
    choices = request.data.get('choices')

    # create the new question in the database
    new_question = Question.objects.create(
        question_text = new_question_text,
        user = request.user
    )

    # create Choice objects for each choice in the list
    for choice in choices:
        Choice.objects.create(
            choice_text = choice,
            question = new_question
        )

    questions = Question.objects.all().order_by('-pub_date')

    # many=True allows multiple instances to be serialized
    question_serializer = QuestionDetailSerializer(questions, many=True)

    response.data = {
        'questions': question_serializer.data
    }

    return response


# Extra challenge, convert this view to DRF API view
def user_polls_list(request, username):
    user = get_object_or_404(CustomUser, username=username)
    questions = Question.objects.filter(user=user)
    
    context = {
        'questions': questions
    }

    return render(request, 'polls/polls-list.html', context)