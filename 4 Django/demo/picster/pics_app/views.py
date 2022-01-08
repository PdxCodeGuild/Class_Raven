from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from users_app.views import login

from .models import Pic

from .forms import PicForm

def home(request):

    pics = Pic.objects.all().order_by('-date_created')

    context = {
        'pics': pics
    }

    return render(request,'pics/home.html', context)


@login_required
def create(request):
    if request.method == 'GET':
        form = PicForm()

        return render(request, 'pics/create.html', {'form': form})

    elif request.method == 'POST':
        form = PicForm(request.POST)

        # retrieve the image from the request data
        form.initial['image'] = request.FILES.get('image')

        if form.is_valid():
            # commit = False will create the item, but won't save it
            new_pic = form.save(commit = False)

            # associate the new pic with the current user
            new_pic.user = request.user

            # commit the final changes
            new_pic.save()

        return redirect(reverse('pics_app:home'))

    
@login_required
def detail(request, pic_id):

    pic = get_object_or_404(Pic, id=pic_id)

    return render(request, 'pics/detail.html', {'pic': pic})


@login_required
def update(request, pic_id):
    pic = get_object_or_404(Pic, id=pic_id)

    if request.method == 'GET':
        # populate the form with data from the current pic
        form = PicForm(instance=pic)

        context = {
            'pic': pic,
            'form': form
        }

        return render(request, 'pics/update.html', context)


    elif request.method == 'POST':
        form = PicForm(request.POST, instance=pic)

        # check if a file was submitted in the form data
        # if so, add it to the form
        image = request.FILES.get('image')
        if image:
            form.initial['image'] = image

        if form.is_valid():
            form.save()

        return redirect(reverse('pics_app:detail', kwargs={'pic_id': pic.id}))


def delete(request, pic_id):
    pic = get_object_or_404(Pic, id=pic_id)

    # if the current user isn't the owner of the pic, redirect home
    if request.user != pic.user:
        return redirect(reverse('pics_app:home'))

    # delete the database object
    pic.delete()

    return redirect(reverse('pics_app:home'))

# this view is used via JS 
@login_required
def like(request, pic_id):
    pic = get_object_or_404(Pic, id=pic_id)

    # add the user if haven't like the pic
    # and remove the user if they have
    if request.user not in pic.likes.all():
        pic.likes.add(request.user)
    else:
        pic.likes.remove(request.user)


    return JsonResponse({
        # boolean indicating if the current user is in the pic's list of likes
        'isLiked': request.user in pic.likes.all(),
        # number of users that have liked the pic
        'likeCount': pic.likes.count()
    })