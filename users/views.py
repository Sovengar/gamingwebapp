from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('appsite-index')
    else:
        form = UserRegisterForm()

    context = {
        "form": form
    }
    return render(request, "users/register.html", context)

def login_view(request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "appsite/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "appsite/login.html", {"message": "Logged out."})
