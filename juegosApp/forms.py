from django import forms

from .models import Juego


class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['titulo', 'genero', 'precio', 'plataforma']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'plataforma': forms.Select(attrs={'class': 'form-select'}),
        }