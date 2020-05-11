from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(request):
    context = {
        "none": 1
    }
    return render(request, "appsite/index.html", context)

def sig_in(request):
    context = {
        "none": 1
    }
    return render(request, "appsite/modules_sign_in.html", context)

def sig_up(request):
    context = {
        "none": 1
    }
    return render(request, "appsite/modules_sign_up.html", context)
