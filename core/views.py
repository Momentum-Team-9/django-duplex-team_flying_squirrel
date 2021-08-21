from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Profile, Snippet


# Create your views here.
def index(request):
    users = User.objects.all()
    
    if request.user.is_authenticated:
        return redirect('feed')
    return render(request, 'core/index.html', {'users': users})


@login_required    
def user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(Profile, user=user)
    
    return render(request, 'core/user_profile.html', {'user': user, 'profile': profile})


@login_required
def feed(request):
    users = User.objects.all()
    
    return render(request, 'core/feed.html', {'users':users})