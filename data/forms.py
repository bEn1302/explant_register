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
        widgets = {
            'schrank': forms.NumberInput(attrs={'class': 'form-control'}),
            'kiste': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PatientUpdateForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('geburtsdatum', 'gewicht')
        widgets = { 
            'geburtsdatum': forms.DateInput(attrs={'class': 'form-control',}),
            'gewicht': forms.NumberInput(attrs={'class': 'form-control',}),
        }

class ReoperationUpdateForm(ModelForm):
    class Meta:
        model = Reoperation
        fields = ('reoperation', 'reoperation_datum')
        widgets = { 
            'reoperation': forms.CheckboxInput(attrs={'class': 'form-control',}),
            'reoperation_datum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date'}),
        }

class InlayUpdateForm(ModelForm):
    class Meta:
        model = Inlay
        fields = ('hersteller', 'modell', 'material', 'groeße')
        widgets = {
            'hersteller': forms.TextInput(attrs={'class': 'form-control'}), 
            'modell': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}), 
            'groeße': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class KopfUpdateForm(ModelForm):
    class Meta:
        model = Kopf
        fields = ('hersteller', 'modell', 'material', 'groeße')
        widgets = {
            'hersteller': forms.TextInput(attrs={'class': 'form-control'}), 
            'modell': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}), 
            'groeße': forms.NumberInput(attrs={'class': 'form-control'}),
        }   

class FemurkomponenteUpdateForm(ModelForm):
    class Meta:
        model = Femurkomponente
        fields = ('hersteller', 'modell', 'material', 'groeße')
        widgets = {
            'hersteller': forms.TextInput(attrs={'class': 'form-control'}), 
            'modell': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}), 
            'groeße': forms.NumberInput(attrs={'class': 'form-control'}),
        }   

class SchaftUpdateForm(ModelForm):
    class Meta:
        model = Schaft
        fields = ('hersteller', 'modell', 'material', 'groeße')
        widgets = {
            'hersteller': forms.TextInput(attrs={'class': 'form-control'}), 
            'modell': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}), 
            'groeße': forms.NumberInput(attrs={'class': 'form-control'}),
        }   

class TibiaplateauUpdateForm(ModelForm):
    class Meta:
        model = Tibiaplateau
        fields = ('hersteller', 'modell', 'material', 'groeße')
        widgets = {
            'hersteller': forms.TextInput(attrs={'class': 'form-control'}), 
            'modell': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}), 
            'groeße': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PfanneUpdateForm(ModelForm):
    class Meta:
        model = Pfanne
        fields = ('hersteller', 'modell', 'material', 'groeße')
        widgets = {
            'hersteller': forms.TextInput(attrs={'class': 'form-control'}), 
            'modell': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}), 
            'groeße': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PatellaersatzUpdateForm(ModelForm):
    class Meta:
        model = Patellaersatz
        fields = ('hersteller', 'modell', 'material', 'groeße')
        widgets = {
            'hersteller': forms.TextInput(attrs={'class': 'form-control'}), 
            'modell': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}), 
            'groeße': forms.NumberInput(attrs={'class': 'form-control'}),
        }             