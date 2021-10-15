from datetime import timedelta

from django.db import models


class Epreuve(models.Model):
    titre = models.CharField(max_length=50, verbose_name="Nom")
    description = models.CharField(max_length=50)
    ponderation = models.FloatField(verbose_name="Maxima")
    dateCreation = models.DateField(auto_now_add=True, editable=False, blank=True, verbose_name='Créée le')
    duree = models.DurationField(default=timedelta(hours=2), verbose_name="Durée")