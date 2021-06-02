from django.contrib import admin
from .models import *

@admin.register(Personne)
class PersonneAdmin(admin.ModelAdmin):
	list_display = (
		"nom", "prenom", "profession", "province", "commune", "lieu_naissance",
		"date_naissance", "cni", "numero_permis", "residence", "photo_1", "photo_2", "autres"
	)
	list_filter = (
		"nom", "prenom", "profession", "province", "commune", "lieu_naissance",
		"date_naissance", "cni", "numero_permis", "residence"
	)
	search_field = (
		"nom", "prenom", "profession", "province", "commune", "lieu_naissance",
		"date_naissance", "cni", "numero_permis", "residence"
	)
	ordering = (
		"nom", "prenom", "profession", "province", "commune", "lieu_naissance",
		"date_naissance", "cni", "numero_permis", "residence"
	)
