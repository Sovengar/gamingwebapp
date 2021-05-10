from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

class Article(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    image = models.ImageField(default='default.jpg', upload_to='article_pics')
    stock = models.IntegerField(default=0)
    release_date = models.DateTimeField(default=timezone.now)
    new_article = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Shopping_cart(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.OneToOneField('users.Client', on_delete=models.CASCADE)
    articles = models.ManyToManyField(Article)

    def __str__(self):
        return self.client.user.username

class Key(models.Model):
    id = models.AutoField(primary_key=True)
    key_value = models.CharField(max_length=17)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    price = models.IntegerField(null=False)
    region = models.CharField(max_length=50)

    def __str__(self):
        return f'Key for article {self.article}'



"""
class Article_on_shopping_cart(models.Model):
    cart = models.ForeignKey(Shopping_cart, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class Opinion(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
"""