from django.contrib import admin
#from import_export.admin import ImportExportModelAdmin
from partner_meet.models import *
#from partner_meet.models import PartnerMeetResource


# Version corrigée
class PartnerMeetAdmin(admin.ModelAdmin):
    model = PartnerMeet
    list_display = ['numero', 'logo', 'url', 'non_affilie', 'categorie', 'nombre_visiteurs_par_mois', 'pourcentage_femmes', 'tranche_age', 'durabilite', 'qualite_du_site']

admin.site.register(PartnerMeet)

# class ComparateurSiteRencontreAdmin(admin.ModelAdmin):
#     model = ComparateurSiteRencontre
#     search_fields = ['nom']
#     list_display = ['nom','genre','logo','url','relation','age','popularite','prix','fonctionnalites']

# admin.site.register(ComparateurSiteRencontre)

class ComparateurAdmin(admin.ModelAdmin):
    model = Comparateur
    search_fields = ['nom']
    list_display = ['nom','genre_find','logo','url','relation','age','popularite','prix','fonctionnalites']

admin.site.register(Comparateur)

# from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
# from partner_meet.models import PartnerMeet

# class PartnerMeetAdmin(ImportExportModelAdmin):
#     list_display = ('numero', 'logo', 'url', 'non_affilie', 'categorie', 'nombre_visiteurs_par_mois', 'pourcentage_femmes', 'tranche_age', 'durabilite', 'qualite_du_site')
#     search_fields = ('numero', 'url', 'categorie')
#     list_filter = ('non_affilie', 'categorie')
#     actions = ['export_as_excel']

#     def export_as_excel(self, request, queryset):
#         # Méthode pour exporter des données en Excel, similaire à celle que j'ai fournie précédemment
#         pass

#     export_as_excel.short_description = "Exporter vers Excel"


