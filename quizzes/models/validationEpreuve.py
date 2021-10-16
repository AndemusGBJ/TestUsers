from datetime import timedelta

from django.conf import settings
from django.db import models
from viewflow.fields import CompositeKey

from quizzes.models.epreuve import Epreuve
from users.models import User


class ValidationEpreuve(models.Model):
    # id = CompositeKey(columns=['id_epreuve', 'user'])
    # id_epreuve = models.ForeignKey(
    #     Epreuve, models.DO_NOTHING,
    #     db_column='id_epreuve'
    # )
    class Meta :
        unique_together = (('epreuve', 'user'))

    epreuve = models.ForeignKey(Epreuve, on_delete=models.CASCADE, primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
        )
    # etudiant = models.ManyToManyField(User)
    dateEpreuve = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    validation = models.BooleanField(verbose_name='Valider')
    cote = models.FloatField()
    duree = models.DurationField(default=timedelta(hours=2))
    dateEpreuve = models.DateField(auto_now_add=True, editable=False, blank=True)
    debut = models.TimeField()
    fin = models.TimeField(auto_now_add=True)


