from webbrowser import get
from django.shortcuts import render, get_object_or_404

from .models import Profile

def profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)

    context = {
        'profile': profile
    }

    return render(request, 'profile.html', context)
