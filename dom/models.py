from django.db import models

# Create your models here.
class Tache(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

class Membre(models.Model):
    nom = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 50)
    mot_de_passe = models.CharField(max_length = 30)

class Foyer(models.Model): 
    name = models.CharField(max_length=20)
    member = models.ManyToManyField(Membre)
    admin = models.IntegerField()
    
   