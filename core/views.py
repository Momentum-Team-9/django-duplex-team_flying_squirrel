from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import User, Profile, Snippet
from .forms import SnippetForm, ProfileForm
from django.db.models import Q
import clipboard


# Create your views here.
def index(request):
    users = User.objects.all()
    
    if request.user.is_authenticated:
        return redirect('feed')
    return render(request, 'core/index.html', {'users': users})


@login_required
def feed(request):
    users = User.objects.all()
    snippets = Snippet.objects.all()
    
    return render(request, 'core/feed.html', {'users':users, 'snippets': snippets})


@login_required    
def user_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(Profile, user=user)
    
    return render(request, 'core/user_profile.html', {'user': user, 'profile': profile})


@login_required
def edit_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(Profile, user=user)

    if request.method == 'GET':
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm(data=request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.profile_image = request.FILES["profile_image"]
            profile.save()
            return redirect('feed')

    return render(
        request,
        'core/edit_profile.html',
        {'form': form}
    )


@login_required
def user(request):
    users = User.objects.all()
    
    return render(request, 'core/users.html', {'users':users})


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


@login_required
def snippet_search(request):
    query = request.GET.get("query")
    search_results = Snippet.objects.filter(Q(title__icontains=query) | Q(code__icontains=query) | Q(language__icontains=query))

    return render(request, "core/feed.html", {"snippets": search_results})


@login_required
def profile_search(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(Profile, user=user)


    query = request.GET.get("query")
    filtered_results = Snippet.objects.filter(created_by_id=request.user.pk)
    search_results = filtered_results.filter(title__icontains=query)

    return render(
        request,
        'core/profile_search.html',
        {'profile': profile, "snippets": search_results}
    )

def copy_snippet(request, snippetPK):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        snippet = Snippet.objects.get(pk=snippetPK)
        user = request.user.username
        copied = Snippet.objects.create(created_by=request.user, title=snippet.title, code=snippet.code, language=snippet.language, copied=0)
        
        copied.save()
        clipboard.copy(snippet.code)
        data ={ 
            "copied": "True"
        }

    return JsonResponse(data)
