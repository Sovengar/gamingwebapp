from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm, SellerRegisterForm, ProfileUserUpdateForm, SellerUserUpdateForm

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
            return redirect('login')
    # if a GET (or any other method) we'll create a blank form
    # This is what we get when we access to the route by navigating/typing
    else:
        form = UserRegisterForm()

    context = {
        "form": form
    }

    return render(request, 'users/register.html', context)

@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = ProfileUserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile updated!')
            return redirect('profile')
    else:
        u_form = ProfileUserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

def register_seller_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        s_form = SellerRegisterForm(request.POST)
        u_form = SellerUserUpdateForm(request.POST, instance=request.user)
        # check whether it's valid:
        if s_form.is_valid() and u_form.is_valid():
            # Saves the form
            s_form.save()
            u_form.save()
            messages.success(request, f'Profile updated!')
            # redirect to a new URL:
            return redirect('profile')
    # if a GET (or any other method) we'll create a blank form
    # This is what we get when we access to the route by navigating/typing
    else:
        s_form = SellerRegisterForm()
        u_form = SellerUserUpdateForm(instance=request.user)

    context = {
        's_form': s_form,
        'u_form': u_form,
        'messages': messages
    }

    return render(request, 'users/register_seller.html', context)

def terms_view(request):
    return render(request, 'users/terms.html')

"""
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
"""

