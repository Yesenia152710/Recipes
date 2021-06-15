from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Author(models.Model):
    au_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=CASCADE)

    def __str__(self):
        return self.au_name


class Recipe(models.Model):
    title = models.CharField(max_length=40)
    ingredience = models.TextField()
    body = models.TextField()
    post_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
