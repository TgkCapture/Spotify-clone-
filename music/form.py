from django import forms
from .models import Music

class AddMusicForm(forms.ModelForm):
    album = forms.CharField(max_length = 500,required=False)
    
    class Meta:
        model=Music
        fields=["title","artist","audio_file","cover_image"]