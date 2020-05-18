from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    price = models.IntegerField(default=0) #TODO REVISAR
    image = models.ImageField(default='default.jpg', upload_to='article_pics')
    stock = models.IntegerField(default=0) #TODO REVISAR
    release_date = models.DateTimeField(default=timezone.now)

class Shopping_cart(models.Model):
    id = models.AutoField(primary_key=True)
    articles = models.ManyToManyField(Article, through='Article_on_shopping_cart')

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cart = models.OneToOneField(Shopping_cart, on_delete=models.CASCADE)
    opinions = models.ManyToManyField(Article, through='Opinion')

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    hours = models.DecimalField(max_digits=2, decimal_places=1)
    plus = models.IntegerField(default=0)







class Article_on_shopping_cart(models.Model):
    cart = models.ForeignKey(Shopping_cart, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class Opinion(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)