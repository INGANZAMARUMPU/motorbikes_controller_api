from django.db import models

class Personne(models.Model):
	nom = models.CharField(max_length=32)
	prenom = models.CharField(max_length=32)
	profession = models.CharField(max_length=32)
	province = models.CharField(max_length=32)
	commune = models.CharField(max_length=32)
	lieu_naissance = models.CharField(max_length=32)
	date_naissance = models.DateField()
	cni = models.CharField(max_length=32)
	numero_permis = models.CharField(max_length=32)
	residence = models.CharField(max_length=32)
	photo_1 = models.FileField(upload_to="photos")
	photo_2 = models.FileField(upload_to="photos")
	autres = models.TextField()
