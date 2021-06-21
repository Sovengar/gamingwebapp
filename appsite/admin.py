from django.contrib import admin
from .models import Game, Shopping_cart, Key, Opinion, Genre

class Shopping_cartInline(admin.StackedInline):
    model = Shopping_cart.keys.through
    extra = 1

class KeyAdmin(admin.ModelAdmin):
    inlines = [Shopping_cartInline]

class Shopping_cartAdmin(admin.ModelAdmin):
    filter_horizontal = ("keys",)

# Register your models here.

admin.site.register(Game)
admin.site.register(Shopping_cart, Shopping_cartAdmin)
admin.site.register(Key, KeyAdmin)
admin.site.register(Opinion)
admin.site.register(Genre)


