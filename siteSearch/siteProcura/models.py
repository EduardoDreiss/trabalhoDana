
from django.db import models

class Musica(models.Model):
    track_id = models.CharField(
        max_length=50, 
        unique=True, 
        primary_key=True,
        help_text="Song unique ID (chave primária da busca)"
    )
    
    track_name = models.CharField(max_length=255)
    track_artist = models.CharField(max_length=255)
    duration_ms = models.IntegerField()
    track_popularity = models.IntegerField(
        help_text="Song Popularity (0-100)"
    )
    playlist_genre = models.CharField(max_length=50)
    
    danceability = models.FloatField(default=0.0) 

    def __str__(self):
        return f"{self.track_name} - {self.track_artist}"

    class Meta:
        verbose_name_plural = "Músicas"