from django.db import models
from viewflow.fields import CompositeKey

from quizzes.models.epreuve import Epreuve
from quizzes.models.etudiant import Etudiant


class ValidationEpreuve(models.Model):
    id = CompositeKey(columns=['epreuve', 'etudiant'])
    epreuve = models.ForeignKey(
        Epreuve, models.DO_NOTHING,
        db_column='epreuve'
    )
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    dateEpreuve = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    validation = models.BooleanField()


