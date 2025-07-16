from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def landing(request):
    context = {'current_time': timezone.now()}
    return render(request, 'music/landing.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'music/login.html', {'current_time': timezone.now()})

def logout_view(request):
    logout(request)
    return redirect('landing')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! You are now logged in.')
            return redirect('landing')
    else:
        form = UserCreationForm()
    return render(request, 'music/signup.html', {'form': form, 'current_time': timezone.now()})

@login_required
def artists(request):
    return render(request, 'music/artists.html', {'current_time': timezone.now()})

@login_required
def listen(request):
    return render(request, 'music/listen.html', {'current_time': timezone.now()})

@login_required
def playlists(request):
    return render(request, 'music/playlists.html', {'current_time': timezone.now()})
def search(request):
    query = request.GET.get('q', '')
    search_type = request.GET.get('type', 'song')
    # Add your search logic here
    context = {
        'query': query,
        'search_type': search_type,
        'current_time': timezone.now(),
        # Add search results to context
    }
    return render(request, 'music/search_results.html', context)