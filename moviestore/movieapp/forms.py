from django import forms
from .models import Movies

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['name','dec','year','img']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dec': forms.Textarea(attrs={'rows': 4, 'cols': 15, 'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control'}),
        }
    