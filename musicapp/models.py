from django.db import models
from datetime import datetime

# Create your models here.
class Artist(models.Model):
    first_name  = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()


class Song(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Lyric(models.Model):
    content = models.CharField(max_length=1000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)