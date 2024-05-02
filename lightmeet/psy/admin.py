from django.contrib import admin
from psy.models import *

class PsyMeetAdmin(admin.ModelAdmin):
    model = PsyMeet
    list_display = ['nom', 'prenom', 'specialite', 'ville', 'departement', 'diplome', 'code_postal', 'adresse', 'genre', 'marque', 'site_web', 'telephone', 'instagram', 'facebook', 'twitter', 'linkedin', 'profil_verifie']

admin.site.register(PsyMeet)