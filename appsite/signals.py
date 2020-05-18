from django.db.models.signals import post_save 
from django.contrib.auth.models import User
from django.dispatch import receiver 
from .models import Article, Article_on_shopping_cart, Shopping_cart, Client, Employee, Opinion

@receiver(post_save, sender=User)
def create_client_cart(sender, instance, created, **kwargs):
    if created:
        mycart = Shopping_cart.objects.create(id=instance.id)
        Client.objects.create(user=instance, cart=mycart)

@receiver(post_save, sender=User)
def save_client(sender, instance, **kwargs):
    instance.client.save()

@receiver(post_save, sender=User)
def save_cart(sender, instance, **kwargs):
    instance.client.cart.save()

