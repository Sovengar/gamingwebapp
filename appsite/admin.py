from django.contrib import admin
from .models import Article, Article_on_shopping_cart, Shopping_cart, Client, Employee, Opinion

# Register your models here.

admin.site.register(Article)
admin.site.register(Article_on_shopping_cart)
admin.site.register(Shopping_cart)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Opinion)