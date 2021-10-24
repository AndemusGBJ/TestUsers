from django.forms import ModelForm
from django import forms

from quizzes.models.reponses import Reponse
from quizzes.models.validationEpreuve import ValidationEpreuve


class ReponseForm(ModelForm):
    contenu = forms.CharField(label='Votre Réponse', widget=forms.Textarea(attrs={
        'class': 'form-control', 'id':'exampleFormControlTextarea1', 'rows':'3'
    }))

    class Meta:
        model=Reponse
        fields  = ["contenu"]