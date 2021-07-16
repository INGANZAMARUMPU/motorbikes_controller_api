from django.contrib import admin
from .models import *

@admin.register(Personne)
class PersonneAdmin(admin.ModelAdmin):
	list_display = (
		"nom", "prenom", "date_naissance", "cni", "no_permi", "no_badge",
		"etat_civil", "telephone", "parking", "residence", "photo_1",
		"photo_2",
	)
	list_filter = (
		"nom", "prenom","date_naissance", "cni", "no_permi", "no_badge",
		"etat_civil", "parking", "residence"
	)
	search_field = (
		"nom", "prenom", "cni", "no_permi", "no_badge",
		"etat_civil", "telephone", "parking", "residence", "autres"
	)
	ordering = (
		"nom", "prenom", "province", "commune", "colline", "date_naissance",
		"no_badge", "etat_civil", "parking", "residence",
	)
