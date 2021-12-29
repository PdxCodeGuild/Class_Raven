from django.shortcuts import (
    render, # helps render html templates
    get_object_or_404, # returns the desired object if it exists or raises a 404 error
    reverse, # lookup the path associated with a view name
)
from django.http import HttpResponse, HttpResponseRedirect ,Http404

# import the models from the Polls app
from .models import Question, Choice

def index(request):
    # return HttpResponse('<h1>Hello world!</h1>')
    
    # get all the questions from the database
    # through the Question model's 'objects' manager
    questions = Question.objects.all().order_by('-pub_date')

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


def create_question(request):
    # the form data is available through the request object
    form = request.POST

    # grab the values from the form
    question_text = form['question_text']
    number_of_choices = int(form['number_of_choices'])

    # create the new question in the database
    new_question = Question()
    new_question.question_text = question_text
    new_question.save()

    # generate a list of choice numbers
    choice_numbers = [number for number in range(1, number_of_choices + 1)]

    # gather data to render into the template
    context = {
        'choice_numbers': choice_numbers,
        'question': new_question
    }

    # render the add_choices.html template using the context data
    return render(request, 'add_choices.html', context)



def add_choices(request):
    form = request.POST

    # find the question object that has the question_id from the form
    question = get_object_or_404(Question, id=form['question_id'])

    for key in form:
        if key.startswith('choice'):
            # create a new Choice database object
            new_choice = Choice()

            # set the choice_text
            # form['choice1'], form['choice2'], etc
            new_choice.choice_text = form[key]

            # associate the choice to the question
            new_choice.question = question

            # save the changes to the database
            new_choice.save()

    # redirect to the home page to view all the polls
    return HttpResponseRedirect(reverse('polls:home'))