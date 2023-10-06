from django import forms
from django.forms import ModelForm
from .models import *

#create a Femurkomponente form
class FemurkomponenteForm(ModelForm):
    class Meta:
        model = Femurkomponente
        fields = ('hersteller', 'modell', 'material', 'groeße')
        
        widgets = {
            'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hersteller'}),
            'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modell'}),
            'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material'}),
            'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Größe'}),
        }

        