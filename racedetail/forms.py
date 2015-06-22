from django import forms
from .models import raceDetail

class raceDetailForm(forms.ModelForm):

    class Meta:
        model = raceDetail
        fields = ('raceName', 'meta',)