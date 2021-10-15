from django.forms import ModelForm
from django import forms

from quizzes.models.etudiant import Etudiant


class EtudiantForm(ModelForm):
    name = forms.CharField(label='Prénom', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    lastname = forms.CharField(label='Nom', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    login = forms.CharField(label='Login', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    pwd = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    telephone = forms.CharField(label='N° Téléphone', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model=Etudiant
        fields  = ("name", "lastname", "login", "pwd", "email","telephone")


