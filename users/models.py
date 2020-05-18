from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    avatar = models.ImageField(default='default_avatar.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        size_300 = (300,300)
        size_40 = (41,41)
  
        img = Image.open(self.image.path)

        #Profile photo
        img.thumbnail(size_300)
        img.save(self.image.path)

        #Avatar photo
        img.thumbnail(size_40)
        img.save(self.avatar.path)