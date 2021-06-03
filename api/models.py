from django.db import models

class Personne(models.Model):
	nom = models.CharField(max_length=32)
	prenom = models.CharField(max_length=32)
	pere = models.CharField(max_length=32)
	mere = models.CharField(max_length=32)
	province = models.CharField(max_length=32)
	commune = models.CharField(max_length=32)
	colline = models.CharField(max_length=32)
	date_naissance = models.DateField()
	cni = models.CharField(max_length=32)
	etat_civil = models.CharField(max_length=32)
	telephone = models.CharField(max_length=32)
	parking = models.CharField(max_length=32)
	residence = models.CharField(max_length=32)
	photo_1 = models.FileField(upload_to="photos")
	photo_2 = models.FileField(upload_to="photos", blank=True, null=True)
	autres = models.TextField(blank=True, null=True)
