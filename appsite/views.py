from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Article, Shopping_cart
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here.

def index_view(request):
    context = {
        "articles": Article.objects.all()
    }
    return render(request, "appsite/index.html", context)

def cart_view(request):
    my_cart = Shopping_cart.objects.get(pk=request.user.id)
    items = my_cart.articles.all()

    context = {
        "articles": items,
        "quantity": items.count()
    }
    return render(request, "appsite/cart.html", context)

def update_cart_view(request, id):
    my_cart = Shopping_cart.objects.get(pk=request.user.id)

    try:
        item = Article.objects.get(id=id)
    except Article.DoesNotExist:
        pass
    except:
        pass

    if not item in my_cart.articles.all():
        my_cart.articles.add(item)
    else:
        my_cart.articles.remove(item)

    return redirect('cart')

class ArticleListView(ListView):
    model = Article 
    template_name = 'appsite/index.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'articles'
    paginate_by = 8

class ArticleDetailView(DetailView):
    model = Article