from django.shortcuts import (
    render, # helps render html templates
    get_object_or_404, # returns the desired object if it exists or raises a 404 error
)
from django.http import HttpResponse, Http404

# import the models from the Polls app
from .models import Question, Choice

def index(request):
    # return HttpResponse('<h1>Hello world!</h1>')
    
    # get all the questions from the database
    # through the Question model's 'objects' manager
    questions = Question.objects.all()

    context = {
        'questions': questions
    }

    # context is a dictionary containing the values we want to use on the template
    # render(request, template_name, context_dict)
    return render(request, 'index.html', context)


def vote(request, choice_id):
    # try:
    #     choice = Choice.objects.get(id=choice_id)

    # except Choice.DoesNotExist:
    #     raise Http404('Choice not found!')

    choice = get_object_or_404(Choice, id=choice_id)

    # increase the choice's vote count
    choice.votes += 1

    # save the updates
    choice.save()

    # send the choice's question object to the results template
    context = {
        'question': choice.question
    }

    return render(request, 'result.html', context)