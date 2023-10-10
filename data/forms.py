from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import *

# ----------------------- Data Insert Forms ----------------------- #
# class LagerortForm(ModelForm):
#     class Meta:
#         model = Lagerort
#         fields = ('schrank', 'kiste')
#         labels = {
#             'schrank': '',
#             'kiste': '',
#         }
#         widgets = {
#             'schrank': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Schrank'}),
#             'kiste': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Kiste'}),
#         }

# class PatientForm(ModelForm):
#     class Meta:
#         model = Patient
#         fields = ('geburtsdatum','gewicht')
#         labels = {
#             'geburtsdatum': '',
#             'gewicht': '',
#         }
#         widgets = { 
#             'geburtsdatum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date',}),
#             'gewicht': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Gewicht'}),
#         }

# class ReoperationForm(ModelForm):
#     class Meta:
#         model = Reoperation
#         fields = ('reoperation', 'reoperation_datum')
#         labels = {
#             'reoperation': '',
#             'reoperation_datum': '',
#         }
#         widgets = { 
#             'reoperation': forms.CheckboxInput(attrs={'class': 'form-control' 'form-check-input', 'placeholder': 'Reoperation'}),
#             'reoperation_datum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date',}),
#         }

# class InlayForm(forms.ModelForm):
#     class Meta:
#         model = Inlay
#         fields = ('hersteller', 'modell', 'material', 'groeße')
#         labels = {
#             'hersteller': '',
#             'modell': '',
#             'material': '',
#             'groeße': '',
#         }
#         widgets = {
#             'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hersteller'}), 
#             'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modell'}),
#             'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material'}), 
#             'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Größe'}),
#         }

# class KopfForm(ModelForm):
#     class Meta:
#         model = Kopf
#         fields = ('hersteller', 'modell', 'material', 'groeße')
#         labels = {
#             'hersteller': '',
#             'modell': '',
#             'material': '',
#             'groeße': '',
#         }
#         widgets = {
#             'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hersteller'}),
#             'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modell'}),
#             'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material'}),
#             'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Größe'}),
#         }   

# class FemurkomponenteForm(ModelForm):
#     class Meta:
#         model = Femurkomponente
#         fields = ('hersteller', 'modell', 'material', 'groeße')
#         labels = {
#             'hersteller': '',
#             'modell': '',
#             'material': '',
#             'groeße': '',
#         }
#         widgets = {
#             'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hersteller'}),
#             'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modell'}),
#             'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material'}),
#             'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Größe'}),
#         }

# class SchaftForm(ModelForm):
#     class Meta:
#         model = Schaft
#         fields = ('hersteller', 'modell', 'material', 'groeße')
#         labels = {
#             'hersteller': '',
#             'modell': '',
#             'material': '',
#             'groeße': '',
#         }
#         widgets = {
#             'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hersteller'}),
#             'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modell'}),
#             'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material'}),
#             'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Größe'}),
#         }   

# class TibiaplateauForm(ModelForm):
#     class Meta:
#         model = Tibiaplateau
#         fields = ('hersteller', 'modell', 'material', 'groeße')
#         labels = {
#             'hersteller': '',
#             'modell': '',
#             'material': '',
#             'groeße': '',
#         }
#         widgets = {
#             'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hersteller'}),
#             'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modell'}),
#             'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material'}),
#             'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Größe'}),
#         }

# class PfanneForm(ModelForm):
#     class Meta:
#         model = Pfanne
#         fields = ('hersteller', 'modell', 'material', 'groeße')
#         labels = {
#             'hersteller': '',
#             'modell': '',
#             'material': '',
#             'groeße': '',
#         }
#         widgets = {
#             'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hersteller'}),
#             'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modell'}),
#             'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material'}),
#             'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Größe'}),
#         }

# class PatellaersatzForm(ModelForm):
#     class Meta:
#         model = Patellaersatz
#         fields = ('hersteller', 'modell', 'material', 'groeße')
#         labels = {
#             'hersteller': '',
#             'modell': '',
#             'material': '',
#             'groeße': '',
#         }
#         widgets = {
#             'hersteller': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hersteller'}),
#             'modell': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modell'}),
#             'material': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material'}),
#             'groeße': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Größe'}),
#         }    

# class ExplantatForm(ModelForm):
#     lagerort_form = LagerortForm()
#     patient_form = PatientForm()
#     reoperation_form = ReoperationForm()
#     inlay_form = InlayForm()
#     kopf_form = KopfForm()
#     femurkomponente_form = FemurkomponenteForm()
#     schaft_form = SchaftForm()
#     tibiaplateau_form = TibiaplateauForm()
#     pfanne_form = PfanneForm()
#     patellaersatz_form = PatellaersatzForm()
    
#     class Meta:
#         model = Explantat
#         fields = ('ursache', 'verfuegbarkeit', 'herkunftsort', 'entnahme_datum', 'eingang_datum', 'bruchgeschehen', 'nutzungsdauer', 'reinigung', 'bild')
#         labels = {
#             'ursache': '', 
#             'verfuegbarkeit': 'Verfügbarkeit',
#             'herkunftsort': '', 
#             'entnahme_datum': '', 
#             'eingang_datum': '', 
#             'bruchgeschehen': '', 
#             'nutzungsdauer': '', 
#             'reinigung': 'Reinigung', 
#             'bild': '',
#         }
#         widgets = {
#             'ursache': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ursache'}), 
#             'verfuegbarkeit': forms.CheckboxInput(attrs={'class': 'form-control form-check-input', 'placeholder': 'Verfügbarkeit'}),
#             'herkunftsort': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Herkunftsort'}), 
#             'entnahme_datum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date',}),
#             'eingang_datum': forms.DateInput(format=('%Y-%m-%d'),attrs={'class': 'form-control', 'type': 'date',}),
#             'bruchgeschehen': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bruchgeschehen'}),
#             'nutzungsdauer': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nutzungsdauer'}), 
#             'reinigung': forms.CheckboxInput(attrs={'class': 'form-control form-check-input', 'placeholder': 'Reinigung'}),
#             'bild': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Bild'}),
#         }

class ExplantatForm(forms.ModelForm):
    lagerort_schrank = forms.IntegerField(label='Schrank Lagerort', required=False)
    lagerort_kiste = forms.IntegerField(label='Kiste Lagerort', required=False)
    
    patient_geburtsdatum = forms.DateField(label='Geburtsdatum Patient', required=False)
    patient_gewicht = forms.FloatField(label='Gewicht Patient', required=False)

    reoperation_reoperation = forms.BooleanField(label='Reoperation', required=False)
    reoperation_reoperation_datum = forms.DateField(label='Reoperationsdatum', required=False)

    inlay_hersteller = forms.CharField(label='Inlay Hersteller', required=False)
    inlay_modell = forms.CharField(label='Inlay Modell', required=False)
    inlay_material = forms.CharField(label='Inlay Material', required=False)
    inlay_groeße = forms.FloatField(label='Inlay Größe', required=False)

    kopf_hersteller = forms.CharField(label='Kopf Hersteller', required=False)
    kopf_modell = forms.CharField(label='Kopf Modell', required=False)
    kopf_material = forms.CharField(label='Kopf Material', required=False)
    kopf_groeße = forms.FloatField(label='Kopf Größe', required=False)

    pfanne_hersteller = forms.CharField(label='Pfanne Hersteller', required=False)
    pfanne_modell = forms.CharField(label='Pfanne Modell', required=False)
    pfanne_material = forms.CharField(label='Pfanne Material', required=False)
    pfanne_groeße = forms.FloatField(label='Pfanne Größe', required=False)

    schaft_hersteller = forms.CharField(label='Schaft Hersteller', required=False)
    schaft_modell = forms.CharField(label='Schaft Modell', required=False)
    schaft_material = forms.CharField(label='Schaft Material', required=False)
    schaft_groeße = forms.FloatField(label='Schaft Größe', required=False)

    femurkomponente_hersteller = forms.CharField(label='Femurkomponente Hersteller', required=False)
    femurkomponente_modell = forms.CharField(label='Femurkomponente Modell', required=False)
    femurkomponente_material = forms.CharField(label='Femurkomponente Material', required=False)
    femurkomponente_groeße = forms.FloatField(label='Femurkomponente Größe', required=False)

    tibiaplateau_hersteller = forms.CharField(label='Tibiaplateau Hersteller', required=False)
    tibiaplateau_modell = forms.CharField(label='Tibiaplateau Modell', required=False)
    tibiaplateau_material = forms.CharField(label='Tibiaplateau Material', required=False)
    tibiaplateau_groeße = forms.FloatField(label='Tibiaplateau Größe', required=False)

    patellaersatz_hersteller = forms.CharField(label='Patellaersatz Hersteller', required=False)
    patellaersatz_modell = forms.CharField(label='Patellaersatz Modell', required=False)
    patellaersatz_material = forms.CharField(label='Patellaersatz Material', required=False)
    patellaersatz_groeße = forms.FloatField(label='Patellaersatz Größe', required=False)

    class Meta:
        model = Explantat
        fields = ('ursache', 'verfuegbarkeit', 'herkunftsort', 'entnahme_datum', 'eingang_datum', 'bruchgeschehen', 'nutzungsdauer', 'reinigung', 'bild')

    def save(self, commit=True):
        explantat = super().save(commit=False)

        lagerort_schrank = self.cleaned_data.get('lagerort_schrank')
        lagerort_kiste = self.cleaned_data.get('lagerort_kiste')

        patient_geburtsdatum = self.cleaned_data.get('patient_geburtsdatum')
        patient_gewicht = self.cleaned_data.get('patient_gewicht')

        reoperation_reoperation = self.cleaned_data.get('reoperation_reoperation')
        reoperation_reoperation_datum = self.cleaned_data.get('reoperation_reoperation_datum')

        inlay_hersteller = self.cleaned_data.get('inlay_hersteller')
        inlay_modell = self.cleaned_data.get('inlay_modell')
        inlay_material = self.cleaned_data.get('inlay_material')
        inlay_groeße = self.cleaned_data.get('inlay_groeße')

        kopf_hersteller = self.cleaned_data.get('kopf_hersteller')
        kopf_modell = self.cleaned_data.get('kopf_modell')
        kopf_material = self.cleaned_data.get('kopf_material')
        kopf_groeße = self.cleaned_data.get('kopf_groeße')

        pfanne_hersteller = self.cleaned_data.get('pfanne_hersteller')
        pfanne_modell = self.cleaned_data.get('pfanne_modell')
        pfanne_material = self.cleaned_data.get('pfanne_material')
        pfanne_groeße = self.cleaned_data.get('pfanne_groeße')

        schaft_hersteller = self.cleaned_data.get('schaft_hersteller')
        schaft_modell = self.cleaned_data.get('schaft_modell')
        schaft_material = self.cleaned_data.get('schaft_material')
        schaft_groeße = self.cleaned_data.get('schaft_groeße')

        femurkomponente_hersteller = self.cleaned_data.get('femurkomponente_hersteller')
        femurkomponente_modell = self.cleaned_data.get('femurkomponente_modell')
        femurkomponente_material = self.cleaned_data.get('femurkomponente_material')
        femurkomponente_groeße = self.cleaned_data.get('femurkomponente_groeße')

        tibiaplateau_hersteller = self.cleaned_data.get('tibiaplateau_hersteller')
        tibiaplateau_modell = self.cleaned_data.get('tibiaplateau_modell')
        tibiaplateau_material = self.cleaned_data.get('tibiaplateau_material')
        tibiaplateau_groeße = self.cleaned_data.get('tibiaplateau_groeße')

        patellaersatz_hersteller = self.cleaned_data.get('patellaersatz_hersteller')
        patellaersatz_modell = self.cleaned_data.get('patellaersatz_modell')
        patellaersatz_material = self.cleaned_data.get('patellaersatz_material')
        patellaersatz_groeße = self.cleaned_data.get('patellaersatz_groeße')

        lagerort, _ = Lagerort.objects.get_or_create(
            schrank=lagerort_schrank,
            kiste=lagerort_kiste
        )

        patient, _ = Patient.objects.get_or_create(
            geburtsdatum=patient_geburtsdatum,
            gewicht=patient_gewicht
        )

        reoperation, _ = Reoperation.objects.get_or_create(
            reoperation=reoperation_reoperation,
            reoperation_datum=reoperation_reoperation_datum
        )

        inlay, _ = Inlay.objects.get_or_create(
            hersteller=inlay_hersteller,
            modell=inlay_modell,
            material=inlay_material,
            groeße=inlay_groeße
        )

        kopf, _ = Kopf.objects.get_or_create(
            hersteller=kopf_hersteller,
            modell=kopf_modell,
            material=kopf_material,
            groeße=kopf_groeße
        )

        pfanne, _ = Pfanne.objects.get_or_create(
            hersteller=pfanne_hersteller,
            modell=pfanne_modell,
            material=pfanne_material,
            groeße=pfanne_groeße
        )

        schaft, _ = Schaft.objects.get_or_create(
            hersteller=schaft_hersteller,
            modell=schaft_modell,
            material=schaft_material,
            groeße=schaft_groeße
        )

        femurkomponente, _ = Femurkomponente.objects.get_or_create(
            hersteller=femurkomponente_hersteller,
            modell=femurkomponente_modell,
            material=femurkomponente_material,
            groeße=femurkomponente_groeße
        )

        tibiaplateau, _ = Tibiaplateau.objects.get_or_create(
            hersteller=tibiaplateau_hersteller,
            modell=tibiaplateau_modell,
            material=tibiaplateau_material,
            groeße=tibiaplateau_groeße
        )

        patellaersatz, _ = Patellaersatz.objects.get_or_create(
            hersteller=patellaersatz_hersteller,
            modell=patellaersatz_modell,
            material=patellaersatz_material,
            groeße=patellaersatz_groeße
        )

        explantat.lagerort = lagerort
        explantat.patient = patient
        explantat.reoperation = reoperation
        explantat.inlay = inlay
        explantat.kopf = kopf
        explantat.pfanne = pfanne
        explantat.schaft = schaft
        explantat.femurkomponente = femurkomponente
        explantat.tibiaplateau = tibiaplateau
        explantat.patellaersatz = patellaersatz

        if commit:
            explantat.save()
        return explantat


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