from django.shortcuts import render

# Create your views here.
context = {
    "dummy_iter" : [1, 2, 3]
}

def index(request):
    return render(request, "todo_list/index.html", context)

def create(request):
    return render(request, "todo_list/create.html")

def update(request):
    return render(request, "todo_list/update.html", context)
    
def delete(request):
    return render(request, "todo_list/delete.html", context)

def completed(request):
    return render(request, "todo_list/completed.html", context)

def signup(request):
    return render(request, "todo_list/signup.html")

def login(request):
    return render(request, "todo_list/login.html")
    
def logout(request):
    return render(request, "todo_list/logout.html")