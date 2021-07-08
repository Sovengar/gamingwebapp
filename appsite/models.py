from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

REGION_CHOICES = (
    ("1", "EU"),
    ("2", "RU")
)

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

"""
class Platform(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
"""

class Game(models.Model):
    name = models.CharField(max_length=50)
    short_desc = models.CharField(max_length=500, default='')
    long_desc = models.CharField(max_length=10000, default='')
    image = models.ImageField(upload_to='game_pics', null=False)
    banner_img = models.ImageField(upload_to='game_pics', null=False)
    stock = models.IntegerField(default=0)
    release_date = models.DateTimeField(default=timezone.now)
    new_game = models.BooleanField(default=True)
    lowest_price = models.IntegerField(null=True, blank=True)
    languages = models.CharField(max_length=200, default='ES')
    system_requirements = models.CharField(max_length=500)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name

class Key(models.Model):
    id = models.AutoField(primary_key=True)
    key_value = models.CharField(max_length=17, unique=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    price = models.IntegerField(null=True)
    region = models.CharField(max_length=50, choices = REGION_CHOICES)
    seller = models.ForeignKey('users.Seller', on_delete=models.CASCADE)
    used = models.BooleanField(default=False)
    owner = models.ForeignKey('users.Client', default=None, blank=False, null=False, on_delete=models.CASCADE)
    #platforms = models.ManyToManyField(Platform)
    
    class Meta:
        ordering = ['-price']

    def __str__(self):
        return f'Key for Game {self.game}'


class Shopping_cart(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.OneToOneField('users.Client', on_delete=models.CASCADE)
    keys = models.ManyToManyField(Key)

    def __str__(self):
        return self.client.user.username

class Opinion(models.Model):
    client = models.ForeignKey('users.Client', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    opinion = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['client', 'game']
        ordering = ['-date_posted']

    def __str__(self):
        return f'From {self.client.user.username} to {self.game.name}' 

"""
class Article_on_shopping_cart(models.Model):
    cart = models.ForeignKey(Shopping_cart, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
"""
