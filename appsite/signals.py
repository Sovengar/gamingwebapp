from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from .models import Article, Shopping_cart, Key
from users.models import  Employee, Client, Seller
from django.dispatch import receiver 


@receiver(post_save, sender=User)
def create_client_cart(sender, instance, created, **kwargs):
    if created:
        c = Client.objects.create(id=instance.id, user=instance)
        Shopping_cart.objects.create(id=instance.id, client=c)

@receiver(post_save, sender=User)
def save_client(sender, instance, **kwargs):
    instance.client.save()

@receiver(post_save, sender=User)
def save_cart(sender, instance, **kwargs):
    sc = Shopping_cart.objects.get(pk=instance.id)
    sc.save()

@receiver(post_save, sender=Key)
def update_article(sender, instance, **kwargs):
    key = Key.objects.get(pk=instance.id)
    article = Article.objects.get(pk=key.article_id) 
    article.stock = article.stock + 1
    article.save()