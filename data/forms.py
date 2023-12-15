from django import forms
from django.forms import ModelForm, inlineformset_factory
from django.forms.widgets import ClearableFileInput
from .models import *

# ----------------------- Cutom Label for file Input ----------------------- #
class CustomClearableFileInput(ClearableFileInput):
    def get_template_substitution_values(self, value):
        values = super().get_template_substitution_values(value)
        values['clear_checkbox_label'] = values['clear_checkbox_label'].replace('Change:', '').strip()
        return values


# ----------------------- Data Insert Forms ----------------------- #
class LagerortForm(ModelForm):
    class Meta:
        model = Lagerort
        fields = ('schrank', 'kiste')
        labels = {
            'schrank': '',
            'kiste': '',
        }
        widgets = {
            'schrank': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Schrank'}),
            'kiste': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Kiste'}),
        }

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('geburtsdatum','gewicht')
        labels = {
            'geburtsdatum': '',
            'gewicht': '',
        }
        widgets = { 
            'geburtsdatum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date',}),
            'gewicht': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Gewicht'}),
        }

class ReoperationForm(ModelForm):
    class Meta:
        model = Reoperation
        fields = ('reoperation', 'reoperation_datum')
        labels = {
            'reoperation': '',
            'reoperation_datum': '',
        }
        widgets = { 
            'reoperation': forms.CheckboxInput(attrs={'class': 'form-control' 'form-check-input', 'placeholder': 'Reoperation'}),
            'reoperation_datum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date',}),
        }

class InlayForm(forms.ModelForm):
    class Meta:
        model = Inlay
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

class KopfForm(ModelForm):
    class Meta:
        model = Kopf
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

class SchaftForm(ModelForm):
    class Meta:
        model = Schaft
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

class TibiaplateauForm(ModelForm):
    class Meta:
        model = Tibiaplateau
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

class PfanneForm(ModelForm):
    class Meta:
        model = Pfanne
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

class PatellaersatzForm(ModelForm):
    class Meta:
        model = Patellaersatz
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

class ExplantatForm(ModelForm):
    lagerort_form = LagerortForm()
    patient_form = PatientForm()
    reoperation_form = ReoperationForm()
    inlay_form = InlayForm()
    kopf_form = KopfForm()
    femurkomponente_form = FemurkomponenteForm()
    schaft_form = SchaftForm()
    tibiaplateau_form = TibiaplateauForm()
    pfanne_form = PfanneForm()
    patellaersatz_form = PatellaersatzForm()
    
    class Meta:
        model = Explantat
        fields = ('ursache', 'verfuegbarkeit', 'herkunftsort', 'entnahme_datum', 'eingang_datum', 'bruchgeschehen', 'nutzungsdauer', 'reinigung', 'bild', 'lagerort', 'patient', 'reoperation', 'inlay', 'kopf', 'schaft', 'pfanne', 'femurkomponente', 'tibiaplateau', 'patellaersatz')
        labels = {
            'ursache': '', 
            'verfuegbarkeit': 'Verfügbarkeit',
            'herkunftsort': '', 
            'entnahme_datum': '', 
            'eingang_datum': '', 
            'bruchgeschehen': '', 
            'nutzungsdauer': '', 
            'reinigung': '', 
            'bild': '',
            'lagerort': '', 
            'patient': '', 
            'reoperation': '',
            'inlay': '', 
            'kopf': '',
            'schaft': '', 
            'pfanne': '', 
            'femurkomponente': '', 
            'tibiaplateau': '', 
            'patellaersatz': ''
        }
        widgets = {
            'ursache': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ursache', 'style': 'height: 150px;'}), 
            'verfuegbarkeit': forms.CheckboxInput(attrs={'class': 'form-control form-check-input', 'placeholder': 'Verfügbarkeit'}),
            'herkunftsort': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Herkunftsort'}), 
            'entnahme_datum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date',}),
            'eingang_datum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date',}),
            'bruchgeschehen': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bruchgeschehen', 'style': 'height: 150px;'}),
            'nutzungsdauer': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nutzungsdauer'}), 
            'reinigung': forms.CheckboxInput(attrs={'class': 'form-control form-check-input', 'placeholder': 'Reinigung'}),
            'bild': CustomClearableFileInput(attrs={'class': 'form-control'}),
            'lagerort': forms.Select(attrs={'class': 'form-select'}),
            'patient': forms.Select(attrs={'class': 'form-select'}),
            'reoperation': forms.Select(attrs={'class': 'form-select'}),
            'inlay': forms.Select(attrs={'class': 'form-select'}),
            'kopf': forms.Select(attrs={'class': 'form-select'}),
            'schaft': forms.Select(attrs={'class': 'form-select'}),
            'pfanne': forms.Select(attrs={'class': 'form-select'}),
            'femurkomponente': forms.Select(attrs={'class': 'form-select'}),
            'tibiaplateau': forms.Select(attrs={'class': 'form-select'}),
            'patellaersatz': forms.Select(attrs={'class': 'form-select'}),
        }

# ----------------------- Data Update Forms ----------------------- #
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