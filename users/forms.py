from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label="",help_text=False, widget=forms.EmailInput(attrs={'class':'form-control form-control-lg bg-light fs-6', 'placeholder': _('Email-Adresse')}))
    first_name = forms.CharField(label="",help_text=False, max_length=25, widget=forms.TextInput(attrs={'class':'form-control form-control-lg bg-light fs-6', 'placeholder':_('Vorname')}))
    last_name = forms.CharField(label="",help_text=False, max_length=25, widget=forms.TextInput(attrs={'class':'form-control form-control-lg bg-light fs-6', 'placeholder':_('Nachname')}))
    
    class Meta:
        model = User
        fields = ('username', 
                  'first_name', 
                  'last_name',
                  'email', 
                  'password1', 
                  'password2')
        
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control form-control-lg bg-light fs-6', 'placeholder': _('Benutzername')})
        self.fields['username'].label = ""

        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control form-control-lg bg-light fs-6', 'placeholder': _('Passwort')})
        self.fields['password1'].label = ""

        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control form-control-lg bg-light fs-6', 'placeholder': _('Passwort bestätigen')})
        self.fields['password2'].label = ""
        
        for fieldname in ['username','password1','password2']:
            self.fields[fieldname].help_text = None