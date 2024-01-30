from django.db import models
from django.contrib.auth.models import User
from apps.etudient.models import Matiere

class Professeur(models.Model):
    telProfesseur = models.CharField(max_length=30, null=True, blank=True)
    user = models.OneToOneField(to=User, on_delete=models.RESTRICT)
    cin = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} '
    
class Enseigner(models.Model):
    matiere = models.ForeignKey(to=Matiere, on_delete=models.RESTRICT)
    professeur = models.ForeignKey(to=Professeur, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.professeur.user.first_name} {self.matiere.nomMatiere}'