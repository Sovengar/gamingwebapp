from django.contrib import admin
from .models import Article, Shopping_cart, Key

class Shopping_cartInline(admin.StackedInline):
    model = Shopping_cart.articles.through
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    inlines = [Shopping_cartInline]

class Shopping_cartAdmin(admin.ModelAdmin):
    filter_horizontal = ("articles",)

# Register your models here.

admin.site.register(Article, ArticleAdmin)
admin.site.register(Shopping_cart, Shopping_cartAdmin)
admin.site.register(Key)


