from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import *

# ----------------------- Data Insert Forms ----------------------- #
class LagerortForm(ModelForm):
    class Meta:
        model = Lagerort
        fields = ('__all__')
        # labels = {
        #     'schrank': '',
        #     'kiste': '',
        # }
        # widgets = {
        #     'schrank': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Schrank'}),
        #     'kiste': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Kiste'}),
        # }

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('__all__')
        # labels = {
        #     'geburtsdatum': '',
        #     'gewicht': '',
        # }
        # widgets = { 
        #     'geburtsdatum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date',}),
        #     'gewicht': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Gewicht'}),
        # }

class ReoperationForm(ModelForm):
    class Meta:
        model = Reoperation
        fields = ('__all__')
        # labels = {
        #     'reoperation': '',
        #     'reoperation_datum': '',
        # }
        # widgets = { 
        #     'reoperation': forms.CheckboxInput(attrs={'class': 'form-control' 'form-check-input', 'placeholder': 'Reoperation'}),
        #     'reoperation_datum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date',}),
        # }

class InlayForm(forms.ModelForm):
    class Meta:
        model = Inlay
        fields = ('__all__')
        # labels = {
        #     'hersteller': '',
        #     'modell': '',
        #     'material': '',
        #     'groeße': '',
        # }
        # widgets = {
        #     'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hersteller'}), 
        #     'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modell'}),
        #     'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material'}), 
        #     'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Größe'}),
        # }

class KopfForm(ModelForm):
    class Meta:
        model = Kopf
        fields = ('__all__')
        # labels = {
        #     'hersteller': '',
        #     'modell': '',
        #     'material': '',
        #     'groeße': '',
        # }
        # widgets = {
        #     'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hersteller'}),
        #     'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modell'}),
        #     'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material'}),
        #     'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Größe'}),
        # }   

class FemurkomponenteForm(ModelForm):
    class Meta:
        model = Femurkomponente
        fields = ('__all__')
        # labels = {
        #     'hersteller': '',
        #     'modell': '',
        #     'material': '',
        #     'groeße': '',
        # }
        # widgets = {
        #     'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hersteller'}),
        #     'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modell'}),
        #     'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material'}),
        #     'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Größe'}),
        # }
    hersteller = forms.CharField(required=False)
    modell = forms.CharField(required=False)
    material = forms.CharField(required=False)
    groeße = forms.FloatField(required=False)

class SchaftForm(ModelForm):
    class Meta:
        model = Schaft
        fields = ('__all__')
        # labels = {
        #     'hersteller': '',
        #     'modell': '',
        #     'material': '',
        #     'groeße': '',
        # }
        # widgets = {
        #     'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hersteller'}),
        #     'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modell'}),
        #     'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material'}),
        #     'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Größe'}),
        # }   
    hersteller = forms.CharField(required=False)
    modell = forms.CharField(required=False)
    material = forms.CharField(required=False)
    groeße = forms.FloatField(required=False)

class TibiaplateauForm(ModelForm):
    class Meta:
        model = Tibiaplateau
        fields = ('__all__')
        # labels = {
        #     'hersteller': '',
        #     'modell': '',
        #     'material': '',
        #     'groeße': '',
        # }
        # widgets = {
        #     'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hersteller'}),
        #     'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modell'}),
        #     'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material'}),
        #     'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Größe'}),
        # }
    hersteller = forms.CharField(required=False)
    modell = forms.CharField(required=False)
    material = forms.CharField(required=False)
    groeße = forms.FloatField(required=False)

class PfanneForm(ModelForm):
    class Meta:
        model = Pfanne
        fields = ('__all__')
        # labels = {
        #     'hersteller': '',
        #     'modell': '',
        #     'material': '',
        #     'groeße': '',
        # }
        # widgets = {
        #     'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hersteller'}),
        #     'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modell'}),
        #     'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material'}),
        #     'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Größe'}),
        # }
    hersteller = forms.CharField(required=False)
    modell = forms.CharField(required=False)
    material = forms.CharField(required=False)
    groeße = forms.FloatField(required=False)

class PatellaersatzForm(ModelForm):
    class Meta:
        model = Patellaersatz
        fields = ('__all__')
        # labels = {
        #     'hersteller': '',
        #     'modell': '',
        #     'material': '',
        #     'groeße': '',
        # }
        # widgets = {
        #     'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hersteller'}),
        #     'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modell'}),
        #     'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material'}),
        #     'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Größe'}),
        # }
    hersteller = forms.CharField(required=False)
    modell = forms.CharField(required=False)
    material = forms.CharField(required=False)
    groeße = forms.FloatField(required=False)       

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
        fields = ('ursache', 'verfuegbarkeit', 'herkunftsort', 'entnahme_datum', 'eingang_datum', 'bruchgeschehen', 'nutzungsdauer', 'reinigung', 'bild')
        # labels = {
        #     'ursache': '', 
        #     'verfuegbarkeit': 'Verfügbarkeit',
        #     'herkunftsort': '', 
        #     'entnahme_datum': '', 
        #     'eingang_datum': '', 
        #     'bruchgeschehen': '', 
        #     'nutzungsdauer': '', 
        #     'reinigung': 'Reinigung', 
        #     'bild': '',
        # }
        # widgets = {
        #     'ursache': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ursache'}), 
        #     'verfuegbarkeit': forms.CheckboxInput(attrs={'class': 'form-control form-check-input', 'placeholder': 'Verfügbarkeit'}),
        #     'herkunftsort': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Herkunftsort'}), 
        #     'entnahme_datum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date',}),
        #     'eingang_datum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date',}),
        #     'bruchgeschehen': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bruchgeschehen'}),
        #     'nutzungsdauer': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nutzungsdauer'}), 
        #     'reinigung': forms.CheckboxInput(attrs={'class': 'form-control form-check-input', 'placeholder': 'Reinigung'}),
        #     'bild': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Bild'}),
        # }

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