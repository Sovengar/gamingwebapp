from django.contrib import admin
from .models import Profile, Employee, Client, Seller

# Register your models here.

admin.site.register(Profile)
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Seller)
