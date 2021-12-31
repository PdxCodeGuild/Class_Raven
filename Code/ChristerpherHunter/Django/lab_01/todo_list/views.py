from django.shortcuts import render

# Create your views here.
context = {
    "dummy_iter" : [1, 2, 3]
}

def index(request):
    
    if request.method == 'GET':
        return render(request, "todo_list/index.html", context)
    
    form = request.POST
    print(form)

def create(request):
    
    if request.method == 'GET':
        return render(request, "todo_list/create.html")
    
    form = request.POST
    print(form)

def update(request):
    
    if request.method == 'GET':
        return render(request, "todo_list/update.html", context)
    
    form = request.POST
    print(form)
    
def delete(request):
    
    if request.method == 'GET':
        return render(request, "todo_list/delete.html", context)
    
    form = request.POST
    print(form)

def completed(request):
    
    if request.method == 'GET':
        return render(request, "todo_list/completed.html", context)
    
    form = request.POST
    print(form)

def signup(request):
    
    if request.method == 'GET':
        return render(request, "todo_list/signup.html")
    
    form = request.POST
    print(form)

def login(request):
    
    if request.method == 'GET':
        return render(request, "todo_list/login.html")
    
    form = request.POST
    print(form)
    
def logout(request):
    return render(request, "todo_list/logout.html")