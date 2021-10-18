from django.db import models

from quizzes.models.questionaire import Questionaire


class Reponse(models.Model):
    contenu = models.TextField()
    pointsObtenus = models.FloatField(null=True, verbose_name='Cotes')
    idQuestion = models.ForeignKey(Questionaire, on_delete=models.CASCADE, null=True, verbose_name='Question')

    def __str__(self):
        return self.contenu