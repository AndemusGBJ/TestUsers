from django.conf import settings
from django.db import models

from quizzes.models.questionaire import Questionaire


class Reponse(models.Model):
    contenu = models.TextField()
    pointsObtenus = models.FloatField(default=0, verbose_name='Cotes')
    idQuestion = models.ForeignKey(Questionaire, on_delete=models.CASCADE, null=True, verbose_name='Question')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )


    def __str__(self):
        return self.contenu