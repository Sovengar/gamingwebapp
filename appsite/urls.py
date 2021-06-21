from django.urls import path
from . import views
from .views import Index_ListView, GameNew_ListView, GameDetailView, OpinionUpdateView
from appsite import views as appsite_views

urlpatterns = [
    #path('', appsite_views.index_view, name='appsite-index'),
    path('', Index_ListView.as_view(), name='appsite-index'), 
    path('newgames/', GameNew_ListView.as_view(), name='appsite-newgames'),
    path('game/<int:pk>/', GameDetailView.as_view(), name='appsite-game_detail'),
    path('game/<int:pk>/update/', appsite_views.OpinionUpdateView, name='appsite-opinion_update'),
    path('game/<int:pk>/delete/', appsite_views.OpinionDeleteView, name='appsite-opinion_delete'),
]

