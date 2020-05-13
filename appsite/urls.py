from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="appsite-index"),
    path("private/", views.private_view, name="appsite-private")
]

