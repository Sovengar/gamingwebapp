from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse


# Create your views here.

def index_view(request):
    context = {
        "user": request.user
    }
    return render(request, "appsite/index.html", context)

def private_view(request):
    if not request.user.is_authenticated:
        return render(request, "appsite/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "appsite/private.html", context)