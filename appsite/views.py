from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
import os
from operator import attrgetter
from django.contrib import messages

from .models import Game, Shopping_cart, Key, Opinion, Genre
from .forms import OpinionForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import FormView
from django.views.generic.edit import FormMixin
from django.contrib.auth.models import User
from django.db.models import Count, Min, Sum, Avg, Q
from django.db import IntegrityError
"""
#Function to return a list with the games found in the query
def get_game_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    
    for q in queries:
        games = Game.objects.filter(stock__gte=1).filter(Q(name__icontains=q) ).distinct()

        for game in games:
            queryset.append(game)
    return list(set(queryset))
"""
#Function to return a list with the games found in the query
def get_game_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    genres = Genre.objects.all()
    aux=False
    genre = None

    for q in queries:
        for genre in genres:
            if q.upper()==genre.name.upper():
                aux=True
                genre = Genre.objects.filter(name=q.capitalize()).first()

    for q in queries:
        if aux==True:
            games = Game.objects.filter(stock__gte=1).filter(genres=genre.name).distinct()
            for game in games:
                queryset.append(game)
        else:
            games = Game.objects.filter(stock__gte=1).filter(Q(name__icontains=q)).distinct()
            for game in games:
                queryset.append(game)
    
    return list(set(queryset))

#View to show the games matching the query
def search_game_queryset(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    try: #Searching for name
        games = sorted(get_game_queryset(query), key=attrgetter('name'), reverse=True)
        context['games'] = games
    except: #Searching for genre
        games = sorted(get_game_queryset(query), reverse=True)
        context['games'] = games

    return render(request, "appsite/search.html", context)

#Index view
"""
def index_view(request):
    context = {}

    new_games = Game.objects.filter(new_game=True).filter(stock__gte=1)
    context['new_games'] = new_games

    games = Game.objects.filter(stock__gte=1)
    context['games'] = games

    return render(request, "appsite/index.html", context)
"""

class Index_ListView(ListView):
    model = Game 
    template_name = 'appsite/index.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'games'
    paginate_by = 8

    def get_queryset(self):
        return Game.objects.filter(stock__gte=1)

    def get_context_data(self, **kwargs):
        context = super(Index_ListView, self).get_context_data(**kwargs)
        context['new_games'] = Game.objects.filter(new_game=True).filter(stock__gte=1)
        return context

@login_required
def cart_view(request):
    my_cart = Shopping_cart.objects.get(pk=request.user.id)
    items = my_cart.keys.all()

    context = {
        "games": items,
        "quantity": items.count()
    }
    return render(request, "appsite/cart.html", context)

@login_required
def update_cart_view(request, id):
    my_cart = Shopping_cart.objects.get(pk=request.user.id)

    try:
        item = Key.objects.get(id=id)
    except Key.DoesNotExist:
        pass
    except:
        pass

    if not item in my_cart.keys.all():
        my_cart.keys.add(item)
    else:
        my_cart.keys.remove(item)

    return redirect('cart')

@login_required
def purchase_cart_view(request, id):
    my_cart = Shopping_cart.objects.get(pk=request.user.id)
    items = my_cart.keys.all()
    
    try:
        for item in items:
            #Update Key
            item.owner = request.user.client
            item.used = True
            item.save()

            #Update Game of the key
            item.game.stock -= 1
            try:
                item.game.lowest_price = Key.objects.filter(game_id=item.game.id).filter(used=False).order_by('price').first().price
            except:
                item.game.lowest_price = None
            
            item.game.save()

            #Remove the key from the cart
            my_cart.keys.remove(item)
    except Key.DoesNotExist:
        pass
    except:
        return HttpResponseForbidden()

    return redirect('profile')

class GameNew_ListView(ListView):
    model = Game 
    template_name = 'appsite/newgames.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'games'
    paginate_by = 8

    def get_queryset(self):
        return Game.objects.filter(stock__gte=1).filter(new_game=True)

class GameDetailView(FormMixin, DetailView):
    model = Game
    form_class = OpinionForm

    def get_context_data(self, **kwargs):
        context = super(GameDetailView, self).get_context_data(**kwargs)
        context['lower_key'] = Key.objects.filter(game_id=self.object.id).filter(used=False).order_by('price').first()
        context['keys'] = Key.objects.filter(game_id=self.object.id).filter(used=False).order_by('price')
        #context['opinions'] = Opinion.objects.filter(game_id=self.object.id)

        if self.request.user.is_authenticated:
            opinion = Opinion.objects.filter(client=self.request.user.client).filter(game_id=self.object.id)
            if opinion.exists():
                context['opinion_bool'] = True
            else:
                context['opinion_bool'] = False
        else:
            context['opinion_bool'] = True

        context['form'] = OpinionForm() #initial={'game': self.object, 'client': self.request.user.client}
        return context
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        form.instance.client = self.request.user.client
        form.instance.game = self.object
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        try:
            form.save()
        except IntegrityError:
            messages.error(self.request, f'Your have already commented on this game')
        except:
            return HttpResponseForbidden()
        
        return super(GameDetailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('appsite-game_detail', kwargs={'pk': self.object.pk})

def partyroom_view(request):
    return render(request, "appsite/partyroom.html")

def OpinionUpdateView(request, pk):
    opinion = Opinion.objects.filter(client=request.user.client).filter(game_id=pk).first()
    form = OpinionForm(request.POST, initial={'opinion': opinion.opinion}, instance=opinion)
    form.fields['opinion'].initial = opinion.opinion
    form['opinion'].value()
    if form.is_valid():
        form.save()
        return redirect('appsite-index')
    else: 
        print("Invalid form")
        print(form.errors.as_json())
   
    context = {
        'form': form
    }

    return render(request, 'appsite/game_detail_update.html', context)

def OpinionDeleteView(request, pk):
    opinion = Opinion.objects.filter(client=request.user.client).filter(game_id=pk).first().delete()
    return redirect('appsite-index')