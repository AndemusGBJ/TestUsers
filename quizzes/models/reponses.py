from django.db import models

from quizzes.models.questionaire import Questionaire


class Reponse(models.Model):
    contenu = models.TextField()
    pointsObtenus = models.FloatField()
    idQuestion = models.ForeignKey(Questionaire, on_delete=models.CASCADE)