from django.contrib import admin
from .models import *

@admin.register(Personne)
class PersonneAdmin(admin.ModelAdmin):
	list_display = (
		"nom", "prenom", "pere", "mere", "province", "commune",\
		"colline", "date_naissance", "cni", "etat_civil", "telephone",\
		"parking", "residence", "photo_1", "photo_2", "autres"
	)
	list_filter = (
		"nom", "prenom", "pere", "mere", "province", "commune",\
		"colline", "date_naissance", "cni", "etat_civil",\
		"telephone", "parking", "residence", "autres"
	)
	search_field = (
		"nom", "prenom", "pere", "mere", "province","commune",\
		"colline", "date_naissance", "cni", "etat_civil",
		"telephone", "parking", "residence", "autres"
	)
	ordering = (
		"nom", "prenom", "pere", "mere", "province", "commune",\
		"colline", "date_naissance", "cni", "etat_civil", \
		"telephone", "parking", "residence", "autres"
	)
