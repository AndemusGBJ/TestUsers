from datetime import timedelta

from django.db import models
from django.template.defaultfilters import slugify


class Epreuve(models.Model):
    titre = models.CharField(max_length=50, verbose_name="Nom")
    description = models.TextField()
    ponderation = models.FloatField(verbose_name="Maxima")
    date = models.DateTimeField( verbose_name='Date')
    duree = models.DurationField(default=timedelta(hours=2), verbose_name="Durée")
    slug = models.SlugField(null=False, unique=True)


    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.titre)
        return super().save(*args, **kwargs)