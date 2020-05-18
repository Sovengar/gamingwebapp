from django.db.models.signals import post_save 
from django.contrib.auth.models import User
from django.dispatch import receiver 
from .models import Article, Shopping_cart, Client, Employee

@receiver(post_save, sender=User)
def create_client_cart(sender, instance, created, **kwargs):
    if created:
        c = Client.objects.create(id=instance.id, user=instance)
        Shopping_cart.objects.create(id=instance.id, user=c)

@receiver(post_save, sender=User)
def save_client(sender, instance, **kwargs):
    instance.client.save()

@receiver(post_save, sender=User)
def save_cart(sender, instance, **kwargs):
    sc = Shopping_cart.objects.get(pk=instance.id)
    sc.save()

