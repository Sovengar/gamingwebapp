from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate

# Create your views here.

def index_view(request):
    context = {
        "user": request.user
    }
    return render(request, "appsite/index.html", context)

def register_view(request):
    context = {
        "none": 1
    }
    return render(request, "appsite/register.html", context)

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

def private_view(request):
    if not request.user.is_authenticated:
        return render(request, "appsite/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "appsite/private.html", context)