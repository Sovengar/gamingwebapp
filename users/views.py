from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def register_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserRegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # Saves the form
            form.save()
            # process the data in form.cleaned_data as required
            username = form.cleaned_data.get('username')
            # Shows a 1 time flash on the template
            messages.success(request, f'Account created for {username}!')
            # redirect to a new URL:
            return redirect('appsite-index')
    # if a GET (or any other method) we'll create a blank form
    # This is what we get when we access to the route by navigating/typing
    else:
        form = UserRegisterForm()

    context = {
        "form": form
    }

    form.fields['password2'].help_text = None

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
