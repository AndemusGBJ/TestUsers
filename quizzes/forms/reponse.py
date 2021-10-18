from django.forms import ModelForm
from django import forms

from quizzes.models.reponses import Reponse
from quizzes.models.validationEpreuve import ValidationEpreuve


class ReponseForm(ModelForm):
    contenu = forms.CharField(label='Votre Réponse', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model=Reponse
        fields  = ["contenu",]