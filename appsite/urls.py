from django.urls import path
from . import views
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name="appsite-index"),
    path('post/<int:pk>/', ArticleDetailView.as_view(), name='appsite-article_detail'),

]

