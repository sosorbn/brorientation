from django.db import models


class Ecole(models.Model):
    id_ecole = models.AutoField(primary_key=True)
    ecole_nom = models.CharField(max_length=200)
    ecole_description = models.CharField(max_length=200)
    lieu = models.CharField(max_length=200)
    lien = models.URLField(default=0)

    def __str__(self):
        return self.ecole_nom

class Domaine(models.Model):
    id_domaine = models.AutoField(primary_key=True)
    domaine_nom = models.CharField(max_length=100)

class DomaineEcole(models.Model):
    id_ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)
    id_domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)

class Intervenant(models.Model):
    id_intervenant = models.AutoField(primary_key=True)
    intervenant_nom = models.CharField(max_length=200, default = 0)
    intervenant_prenom = models.CharField(max_length=200,default = 0)
    intervenant_description = models.CharField(max_length=200, default = 0)
    id_ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)
    id_domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    date_naissance = models.DateField(default=0)
    table_fichier = models.FileField(default=0)
    photo_de_profil = models.ImageField(default=0)
    adresse_mail = models.EmailField(default=0)

    def __str__(self):
        return self.intervenant_nom

class Postulant(models.Model):
    id_postulant = models.AutoField(primary_key=True)
    postulant_nom = models.CharField(max_length=200)
    postulant_prenom = models.CharField(max_length=200)
    postulant_description = models.CharField(max_length=200)
    date_naissance = models.DateField(default=0)
    photo_de_profil = models.ImageField(default=0)
    adresse_mail = models.EmailField(default=0)

class Message(models.Model):
    id_message = models.AutoField(primary_key=True)
    id_postulant = models.ForeignKey(Postulant, on_delete=models.CASCADE)
    id_intervenant = models.ForeignKey(Intervenant, on_delete=models.CASCADE)
    texte = models.CharField(max_length=1000)
    date_heure = models.DateTimeField(default=0)

class MotdePasse(models.Model):
    id_postulant = models.ForeignKey(Postulant, on_delete=models.CASCADE)
    pw = models.CharField(max_length=200)

# Create your models here.
