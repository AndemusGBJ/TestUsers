from django.db import models

class Etudiant(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    login = models.CharField(max_length=50, null=True, blank=True)
    pwd = models.CharField(max_length=50, null=True, blank=True, default="123456789")
    email = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} {self.lastname}"