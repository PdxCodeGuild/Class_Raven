from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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