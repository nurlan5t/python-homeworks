from django.db import models


# Create your models here.
from users.models import User


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='movies/')
    duration = models.CharField(max_length=150)
    age_limit = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies')


class Cast(models.Model):
    movies = models.ManyToManyField(Movie, related_name='cast')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
