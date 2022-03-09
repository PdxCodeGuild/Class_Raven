from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect

from .models import Post

from .forms import PostForm
# @login_required
from django.contrib.auth.decorators import login_required
from django .urls import reverse

# Create your views here.


#Home
def home(request):
    # all to render all the posts, "".order_by('-date_created')" descending order by newest on top
    posts = Post.objects.all().order_by('-date_created')
    #print(posts)
    context = {
        'posts':posts
    }

    return render(request, 'posts/home.html', context)

   
@login_required
def create(request):
    if request.method == 'GET': 

        form = PostForm()

        context = {
        'form': form,

     
        }
        return render(request, 'posts/create.html', context)

    elif request.method == 'POST' and 'image' in request.FILES:
        form = PostForm(request.POST)
        #['images'] implement later
        #form.initial['comment'] = request.FILES.get('comment')
        print(request.POST)
        print(request.FILES)
# redirects to the home page if there are no errorts.
        if form.is_valid():
            form.save(commit=False)
            #new_post = form.save(commit=False)
            #new_post.user = request.user
            #new_post.save()
        return redirect(reverse('post_app:home', kwargs={'post_id': post_id}))    
        #return redirect(reverse('post_app:home', kwargs={'post_id': post_id}))



def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/detail.html', {'post': post})







def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect(reverse('post_app:home', kwargs={'post_id': post_id}))