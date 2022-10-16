from email.policy import default
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime
# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()


class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste,on_delete=CASCADE)
    title = models.CharField(max_length=50)
    date_released = models.DateField(default=datetime.today())
    likes = models.IntegerField()


class Lyric(models.Model):
    song_id = models.ForeignKey(Song,on_delete=CASCADE)
    content = models.CharField(max_length=3000)