from django.db import models
from datetime import datetime
# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self) :
        return self.first_name + " " + self.last_name

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date_released = models.DateField()
    likes = models.IntegerField()

    def __str__(self):
        return self.title

class Lyric(models.Model):
    song_id = models.ForeignKey(Song,on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.song_id.title+ " lyrics"