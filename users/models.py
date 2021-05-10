from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django_countries.fields import CountryField
from django.core.validators import RegexValidator

"""
SEMESTER_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)
class Student(models.Model):
      semester = models.CharField(max_length = 20, choices = SEMESTER_CHOICES, default = '1')
"""

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

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    opinions = models.ManyToManyField('appsite.Article')

    def __str__(self):
        return self.user.username

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    hours = models.DecimalField(max_digits=2, decimal_places=1)
    plus = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    birth_date = models.DateField(auto_now=False)
    city = models.CharField(max_length=100)
    country = CountryField()
    zip = models.CharField(max_length=5)
    street_and_number = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.") #No es una field
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    def calculate_age(born):
        today = date.today()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return age

