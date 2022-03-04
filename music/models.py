from django.db import models
from music.helpers import get_audio_length
from music.validators import validate_is_audio

class Music(models.Model):
    title=models.CharField(max_length=500)
    artist=models.CharField(max_length=500)
    album=models.ForeignKey('Album',on_delete=models.SET_NULL,null=True,blank=True)
    time_length=models.DecimalField(blank=True,max_digits=20,decimal_places=2)
    audio_file=models.FileField(upload_to="music",validators=[validate_is_audio])
    cover_image=models.ImageField(upload_to="music_image/")

    def save(self, *args, **kwargs):
        if not self.time_length:
            audio_length = get_audio_length(self.audio_file) 
            self.time_length =f'{audio_length:.2f}' 

        return super().save(*args, **kwargs)
    
    class META:
        ordering="id"

class Album(models.Model):
    name=models.CharField(max_length=500)
