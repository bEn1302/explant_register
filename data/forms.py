from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from .models import *

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
            'schrank': forms.NumberInput(attrs={'class': 'form-control','placeholder': _('Schrank')}),
            'kiste': forms.NumberInput(attrs={'class': 'form-control','placeholder': _('Kiste')}),
        }

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('geburtsdatum','gewicht')
        labels = {
            'geburtsdatum': _('Geburtsdatum'),
            'gewicht': '',
        }
        widgets = { 
            'geburtsdatum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date',}),
            'gewicht': forms.NumberInput(attrs={'class': 'form-control','placeholder': _('Gewicht')}),
        }

class ReoperationForm(ModelForm):
    class Meta:
        model = Reoperation
        fields = ('reoperation', 'reoperation_datum')
        labels = {
            'reoperation': _('Reoperation'),
            'reoperation_datum': _('Reoperationsdatum'),
        }
        widgets = { 
            'reoperation': forms.CheckboxInput(attrs={'class': 'form-control' 'form-check-input'}),
            'reoperation_datum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date',}),
        }

class KomponentenForm(forms.ModelForm):
    class Meta:
        fields = ('hersteller', 'modell', 'material', 'groeße')
        labels = {
            'hersteller': '',
            'modell': '',
            'material': '',
            'groeße': '',
        }
        widgets = {
            'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Hersteller')}),
            'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Modell')}),
            'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Material')}),
            'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': _('Größe')}),
        }

class InlayForm(KomponentenForm):
    class Meta(KomponentenForm.Meta):
        model = Inlay

class InlayDetailsForm(forms.ModelForm):
    class Meta:
        model = InlayDetails
        fields = ('explantat', 'inlay', 'recycelt')
        widgets = {
            'explantat': forms.Select(attrs={'class': 'form-select'}),
            'inlay': forms.Select(attrs={'class': 'form-select'}),
            'recycelt': forms.CheckboxInput(attrs={'class': 'form-select form-check-input'}),
        }


class KopfForm(KomponentenForm):
    class Meta(KomponentenForm.Meta):
        model = Kopf

class KopfDetailsForm(forms.ModelForm):
    class Meta:
        model = KopfDetails
        fields = ('explantat', 'kopf', 'recycelt')
        widgets = {
            'explantat': forms.Select(attrs={'class': 'form-select'}),
            'kopf': forms.Select(attrs={'class': 'form-select'}),
            'recycelt': forms.CheckboxInput(attrs={'class': 'form-select form-check-input'}),
        }  


class FemurkomponenteForm(KomponentenForm):
    class Meta(KomponentenForm.Meta):
        model = Femurkomponente 

class FemurkomponenteDetailsForm(forms.ModelForm):
    class Meta:
        model = FemurkomponenteDetails
        fields = ('explantat', 'femurkomponente', 'recycelt')
        widgets = {
            'explantat': forms.Select(attrs={'class': 'form-select'}),
            'femurkomponente': forms.Select(attrs={'class': 'form-select'}),
            'recycelt': forms.CheckboxInput(attrs={'class': 'form-select form-check-input'}),
        }  

class SchaftForm(KomponentenForm):
    class Meta(KomponentenForm.Meta):
        model = Schaft

class SchaftDetailsForm(forms.ModelForm):
    class Meta:
        model = SchaftDetails
        fields = ('explantat', 'schaft', 'recycelt')
        widgets = {
            'explantat': forms.Select(attrs={'class': 'form-select'}),
            'schaft': forms.Select(attrs={'class': 'form-select'}),
            'recycelt': forms.CheckboxInput(attrs={'class': 'form-select form-check-input'}),
        } 

    
class TibiaplateauForm(KomponentenForm):
    class Meta(KomponentenForm.Meta):
        model = Tibiaplateau 

class TibiaplateauDetailsForm(forms.ModelForm):
    class Meta:
        model = TibiaplateauDetails
        fields = ('explantat', 'tibiaplateau', 'recycelt')
        widgets = {
            'explantat': forms.Select(attrs={'class': 'form-select'}),
            'tibiaplateau': forms.Select(attrs={'class': 'form-select'}),
            'recycelt': forms.CheckboxInput(attrs={'class': 'form-select form-check-input'}),
        } 


class PfanneForm(KomponentenForm):
    class Meta(KomponentenForm.Meta):
        model = Pfanne 

class PfanneDetailsForm(forms.ModelForm):
    class Meta:
        model = PfanneDetails
        fields = ('explantat', 'pfanne', 'recycelt')
        widgets = {
            'explantat': forms.Select(attrs={'class': 'form-select'}),
            'pfanne': forms.Select(attrs={'class': 'form-select'}),
            'recycelt': forms.CheckboxInput(attrs={'class': 'form-select form-check-input'}),
        }


class PatellaersatzForm(KomponentenForm):
    class Meta(KomponentenForm.Meta):
        model = Patellaersatz

class PatellaersatzDetailsForm(forms.ModelForm):
    class Meta:
        model = PatellaersatzDetails
        fields = ('explantat', 'patellaersatz', 'recycelt')
        widgets = {
            'explantat': forms.Select(attrs={'class': 'form-select'}),
            'patellaersatz': forms.Select(attrs={'class': 'form-select'}),
            'recycelt': forms.CheckboxInput(attrs={'class': 'form-select form-check-input'}),
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
            'verfuegbarkeit': '',
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
            'ursache': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Ursache'), 'style': 'height: 150px;'}), 
            'verfuegbarkeit': forms.CheckboxInput(attrs={'class': 'form-control form-check-input',}),
            'herkunftsort': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Herkunftsort')}), 
            'entnahme_datum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date',}),
            'eingang_datum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date',}),
            'bruchgeschehen': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Bruchgeschehen'), 'style': 'height: 150px;'}),
            'nutzungsdauer': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': _('Nutzungsdauer')}), 
            'reinigung': forms.CheckboxInput(attrs={'class': 'form-control form-check-input',}),
            'bild': forms.FileInput(attrs={'class': 'form-control'}),
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
            'geburtsdatum': forms.DateInput(attrs={'class': 'form-control', 'type': 'date',}),
            'gewicht': forms.NumberInput(attrs={'class': 'form-control',}),
        }

class ReoperationUpdateForm(ModelForm):
    class Meta:
        model = Reoperation
        fields = ('reoperation', 'reoperation_datum')
        widgets = { 
            'reoperation': forms.CheckboxInput(attrs={'class': 'form-check-input',}),
            'reoperation_datum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date'}),
        }

class KomponentenUpdateForm(forms.ModelForm):
    class Meta:
        fields = ('hersteller', 'modell', 'material', 'groeße')
        widgets = {
            'hersteller': forms.TextInput(attrs={'class': 'form-control'}), 
            'modell': forms.TextInput(attrs={'class': 'form-control'}),
            'material': forms.TextInput(attrs={'class': 'form-control'}), 
            'groeße': forms.NumberInput(attrs={'class': 'form-control'}),
        }        

class InlayUpdateForm(KomponentenUpdateForm):
    class Meta(KomponentenUpdateForm.Meta):
        model = Inlay

class KopfUpdateForm(KomponentenUpdateForm):
    class Meta(KomponentenUpdateForm.Meta):
        model = Kopf   

class FemurkomponenteUpdateForm(KomponentenUpdateForm):
    class Meta(KomponentenUpdateForm.Meta):
        model = Femurkomponente   

class SchaftUpdateForm(KomponentenUpdateForm):
    class Meta(KomponentenUpdateForm.Meta):
        model = Schaft   

class TibiaplateauUpdateForm(KomponentenUpdateForm):
    class Meta(KomponentenUpdateForm.Meta):
        model = Tibiaplateau

class PfanneUpdateForm(KomponentenUpdateForm):
    class Meta(KomponentenUpdateForm.Meta):
        model = Pfanne

class PatellaersatzUpdateForm(KomponentenUpdateForm):
    class Meta(KomponentenUpdateForm.Meta):
        model = Patellaersatz             

# ----------------------- User Profile Forms ----------------------- #
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'state', 'zip_code', 'city', 'profile_picture']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email']