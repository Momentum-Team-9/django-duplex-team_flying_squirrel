from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Profile, Snippet
from .forms import SnippetForm


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
    snippets = Snippet.objects.all()
    
    return render(request, 'core/feed.html', {'users':users, 'snippets': snippets})


@login_required
def snippet(request, pk):
    users = User.objects.all()
    snippet = Snippet.objects.all()

    return


@login_required
def add_snippet(request, pk):
    if request.method == 'GET':
        form = SnippetForm()
    else: 
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            return redirect(to='feed')

    return render(
        request,
        'core/add_snippet.html',
        {'form': form}
    )


@login_required
def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == 'GET':
        form = SnippetForm(instance=snippet)
    else:
        form = SnippetForm(data=request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect(to='feed')

    return render(
        request,
        'core/edit_snippet.html',
        {'form': form, 'snippet': snippet}
    )