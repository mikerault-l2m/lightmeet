from django.contrib import admin
from django.urls import path
from django.shortcuts import render

from partner_meet.models import PartnerMeet

class PartnerMeetAdmin(admin.ModelAdmin):
    list_display = ('numero', 'logo', 'url', 'non_affilie', 'categorie', 'nombre_visiteurs_par_mois', 'pourcentage_femmes', 'tranche_age', 'durabilite', 'qualite_du_site')
    search_fields = ('numero', 'url', 'categorie')
    list_filter = ('non_affilie', 'categorie')
    actions = ['export_as_excel']

    def import_button(self, request, *args, **kwargs):
        context = dict(
            self.admin_site.each_context(request),
        )
        return render(request, 'admin/import_button.html', context=context)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import/', self.admin_site.admin_view(self.import_button), name='site_web_import'),
        ]
        return custom_urls + urls

    def export_as_excel(self, request, queryset):
        # Méthode pour exporter des données en Excel, similaire à celle que j'ai fournie précédemment
        pass

    export_as_excel.short_description = "Exporter vers Excel"

admin.site.register(PartnerMeet, PartnerMeetAdmin)
