from django import forms
from django.forms import ModelForm
from .models import *

#create a Femurkomponente form
class FemurkomponenteForm(ModelForm):
    class Meta:
        model = Femurkomponente
        fields = ('hersteller', 'modell', 'material', 'groeße')
        labels = {
            'hersteller': '',
            'modell': '',
            'material': '',
            'groeße': '',
        }
        
        widgets = {
            'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hersteller'}),
            'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modell'}),
            'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material'}),
            'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Größe'}),
        }

#Create a Explantat form
# class ExplantatForm(ModelForm):
#     class Meta:
#         model = Explantat
#         fields = ('__all__')


# Update Forms
class LagerortUpdateForm(ModelForm):
    class Meta:
        model = Lagerort
        fields = ('schrank', 'kiste')

class PatientUpdateForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('geburtsdatum', 'gewicht')
        widgets = { 
            'geburtsdatum': forms.DateInput(),
        }

class ReoperationUpdateForm(ModelForm):
    class Meta:
        model = Reoperation
        fields = ('reoperation', 'reoperation_datum')
        widgets = { 
            'reoperation_datum': forms.DateInput(),
        }

class InlayUpdateForm(ModelForm):
    class Meta:
        model = Inlay
        fields = ('hersteller', 'modell', 'material', 'groeße')

class KopfUpdateForm(ModelForm):
    class Meta:
        model = Kopf
        fields = ('hersteller', 'modell', 'material', 'groeße')   

class FemurkomponenteUpdateForm(ModelForm):
    class Meta:
        model = Femurkomponente
        fields = ('hersteller', 'modell', 'material', 'groeße')   

class SchaftUpdateForm(ModelForm):
    class Meta:
        model = Schaft
        fields = ('hersteller', 'modell', 'material', 'groeße')   

class TibiaplateauUpdateForm(ModelForm):
    class Meta:
        model = Tibiaplateau
        fields = ('hersteller', 'modell', 'material', 'groeße')

class PfanneUpdateForm(ModelForm):
    class Meta:
        model = Pfanne
        fields = ('hersteller', 'modell', 'material', 'groeße')

class PatellaersatzUpdateForm(ModelForm):
    class Meta:
        model = Patellaersatz
        fields = ('hersteller', 'modell', 'material', 'groeße')             