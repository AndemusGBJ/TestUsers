from django.db import models

from quizzes.models.epreuve import Epreuve


class Questionaire(models.Model):
    titre = models.CharField(max_length=250)
    contenu = models.TextField()
    ponderation = models.FloatField()
    corrige = models.TextField()
    idEpreuve = models.ForeignKey(Epreuve, on_delete=models.CASCADE)