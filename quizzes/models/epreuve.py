from datetime import timedelta

from django.db import models


class Epreuve(models.Model):
    titre = models.CharField(max_length=50, verbose_name="Nom")
    description = models.TextField()
    ponderation = models.FloatField(verbose_name="Maxima")
    dateCreation = models.DateField(auto_now_add=True, editable=False, blank=True, verbose_name='Créée le')
    duree = models.DurationField(default=timedelta(hours=2), verbose_name="Durée")


    def __str__(self):
        return self.titre