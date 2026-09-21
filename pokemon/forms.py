from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['poke_id', 'name', 'height', 'weight', 'sprite_url']
        widgets = {
            'poke_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 25'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Pikachu'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'Altura en m'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'Peso en kg'}),
            'sprite_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
        }