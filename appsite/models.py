from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    price = models.IntegerField(null=False)
    image = models.ImageField(default='default.jpg', upload_to='article_pics')
    stock = models.IntegerField(default=1)
    release_date = models.DateTimeField(default=timezone.now)
    new_article = models.BooleanField(default=True)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    opinions = models.ManyToManyField(Article)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    hours = models.DecimalField(max_digits=2, decimal_places=1)
    plus = models.IntegerField(default=0)

class Shopping_cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Client, on_delete=models.CASCADE)
    articles = models.ManyToManyField(Article)

"""
class Article_on_shopping_cart(models.Model):
    cart = models.ForeignKey(Shopping_cart, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class Opinion(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
"""