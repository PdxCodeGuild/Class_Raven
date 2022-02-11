from django.shortcuts import render
from .models import KeyId, KeyInstance, Lock
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from catalog.forms import RenewKeyForm


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

    context = {                    # COMMENTED OUT VISITS COUNTER ON HTML FOR NOW
        'num_keys': num_keys,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with data in context variable
    return render(request, 'index.html', context=context)

class KeyListView(generic.ListView):
    model = KeyId
    paginate_by = 50

class KeyDetailView(generic.DetailView):
    model = KeyId

class LoanedKeysByUserListView(LoginRequiredMixin,generic.ListView):
    # View listing keys on loan to current user.
    model = KeyInstance
    template_name ='catalog/keyinstance_list_borrowed_user.html'
    paginate_by = 5

    def get_queryset(self):
        return KeyInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class LoanedKeysAllListView(PermissionRequiredMixin, generic.ListView):
    # View listing all keyss on loan. Only visible to users with can_mark_returned permission.
    model = KeyInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/keyinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        return KeyInstance.objects.filter(status__exact='o').order_by('due_back')

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_key_librarian(request, pk):
            #View function for renewing a specific KeyInstance by admin.
    key_instance = get_object_or_404(KeyInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

      
        form = RenewKeyForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            #write to the model due_back field
            key_instance.due_back = form.cleaned_data['renewal_date']
            key_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed'))

    # If  GET create the default form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewKeyForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'key_instance': key_instance,
    }

    return render(request, 'catalog/key_renew_admin.html', context)

# NEW BLOCK ================================================================
#NOT SAVED 

class RequestedKeysAllListView(PermissionRequiredMixin, generic.ListView):
    # View listing all keyss on loan. Only visible to users with can_mark_returned permission.
    model = KeyInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/key_requests.html'
    paginate_by = 10

    def get_queryset(self):
        return KeyInstance.objects.filter(status__exact='r').order_by('due_back')

@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def request_key_librarian(request, pk):
            #View function for renewing a specific KeyInstance by admin.
    key_instance = get_object_or_404(KeyInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

      
        form = RenewKeyForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            #write to the model due_back field
            key_instance.due_back = form.cleaned_data['renewal_date']
            key_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed'))

    # If  GET create the default form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewKeyForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'key_instance': key_instance,
    }

    return render(request, 'catalog/key_renew_admin.html', context)
