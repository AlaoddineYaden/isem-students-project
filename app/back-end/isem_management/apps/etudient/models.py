from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator




class Departement(models.Model):
    nomDepartement = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nomDepartement}'
    

class Filiere(models.Model):
    nomFiliere = models.CharField(max_length=255)
    departement = models.ForeignKey(to=Departement, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nomFiliere}'
    

class Etudient(models.Model):
    cne = models.CharField(max_length=30, unique=True)
    cin = models.CharField(max_length=30, unique=True)
    nomEtudientAr = models.CharField(max_length=255, null=True, blank=True, )
    prenomEtudientAr = models.CharField(max_length=255, null=True, blank=True, )
    adresse = models.TextField()
    adresseAr = models.TextField(null=True, blank=True, )
    sexe = models.CharField(max_length=20, null=True, blank=True)
    villeDeNaissance = models.CharField(max_length=255)
    villeDeNaissanceAr = models.CharField(max_length=255, null=True, blank=True)
    dateDeNaissance = models.DateField()
    telEtudient = models.CharField(max_length=30, null=True, blank=True)
    situation_familiale = models.CharField(max_length=50, null=True, blank=True)
    user = models.OneToOneField(to=User, on_delete=models.RESTRICT)
    filiere = models.ForeignKey(to=Filiere, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    


    
class Module(models.Model):
    nomModule = models.CharField(max_length=255)
    coefficient = models.FloatField()
    filiere = models.ForeignKey(to=Filiere, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.filiere.nomFiliere} {self.nomModule}'
    
class Matiere(models.Model):
    nomMatiere = models.CharField(max_length=255)
    coefficient = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    publier = models.BooleanField(default=False)
    module = models.ForeignKey(to=Module, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.module.nomModule} {self.nomMatiere}'
    

class Note(models.Model):
    note_type = models.CharField(max_length=255)
    coefficient = models.FloatField()
    annee = models.CharField(max_length=16)
    etudient = models.ForeignKey(to=Etudient, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.etudient.user.first_name} {self.note_type}'
    

    
