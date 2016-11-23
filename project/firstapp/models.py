from django.db import models

# Create your models here.
class Post(models.Model):
    sexe=models.CharField(max_length=40)
    nom=models.CharField(max_length=40)
    pays = models.CharField(max_length=40)
    age = models.IntegerField()
    contact=models.CharField(max_length=40)
    mail = models.CharField(max_length=80)
    tel=models.IntegerField()
    h=models.IntegerField()
    mn=models.IntegerField()
    jour=models.IntegerField()
    mois=models.IntegerField()
    annee=models.IntegerField()
    traitement=models.CharField(max_length=40)
    description = models.TextField()


    def __str__(self):
        return self.nom
# Create your models here.
