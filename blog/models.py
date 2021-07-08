from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

GENRE_CHOICES = (
    ("Guides", "Guides"),
    ("News", "News"),
    ("IRL", "IRL"),
    ("Games", "Games"),
    ("Other", "Other"),
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50, choices = GENRE_CHOICES, blank=False, null=False, default='a')
    img_prepost = models.ImageField(upload_to='blog_pics', blank=False, null=False, default='default.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-post_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    author = models.ForeignKey('users.Client', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['author', 'post']
        ordering = ['-date_posted']

    def __str__(self):
        return f'From {self.author.user.username} to Post {self.post.title}' 