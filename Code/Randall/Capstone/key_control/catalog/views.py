from django.shortcuts import render
from .models import KeyId, KeyInstance, Lock
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    #View function for home page of site.

    # Generate counts of some of the main objects
    num_keys = KeyId.objects.all().count()
    num_instances = KeyInstance.objects.all().count()
    # Available keys (status = 'a')
    num_instances_available = KeyInstance.objects.filter(status__exact='a').count()
    # Show a count of the number of times user has visited the page
    num_visits = request.session.get('num_visits', 0) #Starts over after server restart
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_keys': num_keys,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class KeyListView(generic.ListView):
    model = KeyId
    paginate_by = 50

class KeyDetailView(generic.DetailView):
    model = KeyId

class LoanedKeysByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = KeyInstance
    template_name ='catalog/keyinstance_list_borrowed_user.html'
    paginate_by = 5

    def get_queryset(self):
        return KeyInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

