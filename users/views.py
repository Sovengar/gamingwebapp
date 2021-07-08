from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import GenericViewError
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserRegisterForm, ProfileUpdateForm, SellerRegisterForm, ProfileUserUpdateForm, SellerUserUpdateForm, SellKeyForm
from .models import Seller, Client
from appsite.models import Game, Key
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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

def hasSellerAcc_check(user):
    if user.is_superuser:
        return True
    else:
        try:
            if user.client.seller:
                return False
            else:
                return True
        except Seller.DoesNotExist:
            return True
     
def hasSellerValidAcc_check(user):
    if user.is_superuser:
        return True
    else:
        return user.client.seller.valid

@login_required
@user_passes_test(hasSellerAcc_check, login_url='/', redirect_field_name=None)
def register_seller_view(request):
    if request.method == 'POST':
        s_form = SellerRegisterForm(request.POST, request.FILES)
        u_form = SellerUserUpdateForm(request.POST, instance=request.user)

        if s_form.is_valid() and u_form.is_valid():
            c = Client.objects.get(id=request.user.id)
            seller = Seller.objects.create(id=c.id, client=c)
            s_form = SellerRegisterForm(request.POST, request.FILES, instance=seller)
            # Saves the form
            s_form.save()
            u_form.save()

            # redirect to a new URL:
            return redirect('profile')
        else: 
            print("Invalid form")
            print(s_form.errors.as_json())
    
    else:
        s_form = SellerRegisterForm()
        u_form = SellerUserUpdateForm(instance=request.user)

    context = {
        's_form': s_form,
        'u_form': u_form
    }

    return render(request, 'users/register_seller.html', context)

@login_required
@user_passes_test(hasSellerValidAcc_check, login_url='/', redirect_field_name=None)
def seller_view(request):
    if request.method == 'POST':
        form = SellKeyForm(request.POST)
        if form.is_valid():
            new_key = form.save(commit=False)
            new_key.seller_id = request.user.client.seller.id #new_key.some_field = 'some_value'
            new_key.owner_id = request.user.client.seller.id
            new_key.save()
            form.save_m2m()
            return redirect('profile')
        else: 
            print("Invalid form")
            print(form.errors.as_json())
   
    else:
        form = SellKeyForm()
    
    context = {
        'form': form,
        'games': Game.objects.all() 
    }

    return render(request, 'users/sellkey.html', context)

class Keys_ListView(LoginRequiredMixin, ListView):
    model = Key 
    template_name = 'users/keys.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'keys'
    paginate_by = 10

    def get_queryset(self):
        return Key.objects.filter(owner=self.request.user.client.id)

    def get_context_data(self, **kwargs):
        context = super(Keys_ListView, self).get_context_data(**kwargs)
        context['keys_selling'] = Key.objects.filter(seller=self.request.user.client.id).filter(used=False)
        context['keys_sold'] = Key.objects.filter(seller=self.request.user.client.id).filter(used=True)
        context['keys_bought'] = Key.objects.filter(owner=self.request.user.client.id).filter(used=True)
        return context

def terms_view(request):
    return render(request, 'users/terms.html')

def faq_view(request):
    return render(request, 'users/faq.html')

