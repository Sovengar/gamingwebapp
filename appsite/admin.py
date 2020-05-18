from django.contrib import admin
from .models import Article, Shopping_cart, Client, Employee

# Register your models here.

admin.site.register(Article)
admin.site.register(Shopping_cart)
admin.site.register(Client)
admin.site.register(Employee)
