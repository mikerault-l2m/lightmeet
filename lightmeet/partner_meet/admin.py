from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import PartnerMeet, PartnerMeetResource

@admin.register(PartnerMeet)
class PartnerMeetAdmin(ImportExportModelAdmin):
    resource_class = PartnerMeetResource
    list_display = ['numero', 'logo', 'url', 'non_affilie', 'categorie', 'nombre_visiteurs_par_mois', 'pourcentage_femmes', 'tranche_age', 'durabilite', 'qualite_du_site']

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

# admin.site.register(PartnerMeet, PartnerMeetAdmin)
