from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signin", views.sig_in, name="sign_in")
]

