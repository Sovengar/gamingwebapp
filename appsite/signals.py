from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from .models import Game, Shopping_cart, Key
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
def update_game(sender, instance, created, **kwargs):
    game = Game.objects.get(pk=instance.game_id)
    if created:
        game.stock += 1
        try:
            game.lowest_price = Key.objects.filter(game_id=game.id).filter(used=False).order_by('price').first().price
        except:
            game.lowest_price = None
    game.save()