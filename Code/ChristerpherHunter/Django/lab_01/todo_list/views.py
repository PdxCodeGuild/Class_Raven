from django.shortcuts import render

# Create your views here.
dummy_iter = {
    1: "one",
    2: "two",
    3: "three"
}

def index(request):
    return render(request, "todo_list/index.html", dummy_iter)

def create(request):
    return render(request, "todo_list/create.html")

