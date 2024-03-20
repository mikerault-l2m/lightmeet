from django.contrib import admin
from psy.models import *

class PsyMeetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'specialite', 'localisation', 'anciennete', 'date_creation')
    search_fields = ('nom', 'prenom', 'specialite')
    list_filter = ('specialite', 'localisation')
    readonly_fields = ('date_creation',)


admin.site.register(PsyMeet,PsyMeetAdmin)