from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from psy.models import PsyMeet
from accounts.models import *  # Si nécessaire, importez ce dont vous avez besoin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _  # Importez gettext_lazy pour les chaînes traduisibles
import time
# Étape 1 : Lancement de la page principale Lightmeet :

start = time.time()
class Home(TemplateView):
    model = Lightener
    template_name = 'partner_meet/Home.html'
    # Si vous avez besoin de traduire le nom du modèle ou le nom du template, utilisez gettext_lazy ici

end = time.time()
elapsed = end - start
print(f'Temps d\'affichage de LightMeet : {elapsed:.2f}ms')  # Utilisez .2f pour la précision

# Étape 2

start = time.time()
class PsyMeetHome(ListView):
    model = PsyMeet
    context_object_name = _("psymeet")  # Utilisez gettext_lazy pour les contextes traduisibles
    template_name = "psy/psymeet_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['DEPARTEMENT_CHOICES'] = [
            (code, _(label)) for code, label in [
                ("01", "01 - Ain"),
                ("02", "02 - Aisne"),
                ("03", "03 - Allier"),
                ("04", "04 - Alpes-de-Haute-Provence"),
                ("05", "05 - Hautes-Alpes"),
                ("06", "06 - Alpes-Maritimes"),
                ("07", "07 - Ardèche"),
                ("08", "08 - Ardennes"),
                ("09", "09 - Ariège"),
                ("10", "10 - Aube"),
                ("11", "11 - Aude"),
                ("12", "12 - Aveyron"),
                ("13", "13 - Bouches-du-Rhône"),
                ("14", "14 - Calvados"),
                ("15", "15 - Cantal"),
                ("16", "16 - Charente"),
                ("17", "17 - Charente-Maritime"),
                ("18", "18 - Cher"),
                ("19", "19 - Corrèze"),
                ("21", "21 - Côte-d'Or"),
                ("22", "22 - Côtes-d'Armor"),
                ("23", "23 - Creuse"),
                ("24", "24 - Dordogne"),
                ("25", "25 - Doubs"),
                ("26", "26 - Drôme"),
                ("27", "27 - Eure"),
                ("28", "28 - Eure-et-Loir"),
                ("29", "29 - Finistère"),
                ("2A", "2A - Corse-du-Sud"),
                ("2B", "2B - Haute-Corse"),
                ("30", "30 - Gard"),
                ("31", "31 - Haute-Garonne"),
                ("32", "32 - Gers"),
                ("33", "33 - Gironde"),
                ("34", "34 - Hérault"),
                ("35", "35 - Ille-et-Vilaine"),
                ("36", "36 - Indre"),
                ("37", "37 - Indre-et-Loire"),
                ("38", "38 - Isère"),
                ("39", "39 - Jura"),
                ("40", "40 - Landes"),
                ("41", "41 - Loir-et-Cher"),
                ("42", "42 - Loire"),
                ("43", "43 - Haute-Loire"),
                ("44", "44 - Loire-Atlantique"),
                ("45", "45 - Loiret"),
                ("46", "46 - Lot"),
                ("47", "47 - Lot-et-Garonne"),
                ("48", "48 - Lozère"),
                ("49", "49 - Maine-et-Loire"),
                ("50", "50 - Manche"),
                ("51", "51 - Marne"),
                ("52", "52 - Haute-Marne"),
                ("53", "53 - Mayenne"),
                ("54", "54 - Meurthe-et-Moselle"),
                ("55", "55 - Meuse"),
                ("56", "56 - Morbihan"),
                ("57", "57 - Moselle"),
                ("58", "58 - Nièvre"),
                ("59", "59 - Nord"),
                ("60", "60 - Oise"),
                ("61", "61 - Orne"),
                ("62", "62 - Pas-de-Calais"),
                ("63", "63 - Puy-de-Dôme"),
                ("64", "64 - Pyrénées-Atlantiques"),
                ("65", "65 - Hautes-Pyrénées"),
                ("66", "66 - Pyrénées-Orientales"),
                ("67", "67 - Bas-Rhin"),
                ("68", "68 - Haut-Rhin"),
                ("69", "69 - Rhône"),
                ("70", "70 - Haute-Saône"),
                ("71", "71 - Saône-et-Loire"),
                ("72", "72 - Sarthe"),
                ("73", "73 - Savoie"),
                ("74", "74 - Haute-Savoie"),
                ("75", "75 - Paris"),
                ("76", "76 - Seine-Maritime"),
                ("77", "77 - Seine-et-Marne"),
                ("78", "78 - Yvelines"),
                ("79", "79 - Deux-Sèvres"),
                ("80", "80 - Somme"),
                ("81", "81 - Tarn"),
                ("82", "82 - Tarn-et-Garonne"),
                ("83", "83 - Var"),
                ("84", "84 - Vaucluse"),
                ("85", "85 - Vendée"),
                ("86", "86 - Vienne"),
                ("87", "87 - Haute-Vienne"),
                ("88", "88 - Vosges"),
                ("89", "89 - Yonne"),
                ("90", "90 - Territoire de Belfort"),
                ("91", "91 - Essonne"),
                ("92", "92 - Hauts-de-Seine"),
                ("93", "93 - Seine-Saint-Denis"),
                ("94", "94 - Val-de-Marne"),
                ("95", "95 - Val-d'Oise"),
                ("971", "971 - Guadeloupe"),
                ("972", "972 - Martinique"),
                ("973", "973 - Guyane"),
                ("974", "974 - La Réunion"),
                ("976", "976 - Mayotte")
            ]
        ]
        context['DIPLOME_CHOICES'] = [
            ("Diplômé d'état", _("Diplômé d'état")),
            ("Indépendant", _("Indépendant")),
        ]
        context['SPECIALITE_CHOICES'] = [
            ("Psychologie clinique", _("Psychologie clinique")),
            ("Psychologie du travail", _("Psychologie du travail")),
            ("Psychologie sociale", _("Psychologie sociale")),
        ]
        return context

    def get_queryset(self):
        start = time.time()
        queryset = super().get_queryset()

        departement = self.request.GET.get('departement')
        if departement:
            queryset = queryset.filter(departement=departement)

        diplome = self.request.GET.get('diplome')
        if diplome:
            queryset = queryset.filter(diplome=diplome)

        specialite = self.request.GET.get('specialite')
        if specialite:
            queryset = queryset.filter(specialite=specialite)

        return queryset
end = time.time()
elapsed = end - start
print(f'Temps d\'affichage des critères des sites des thérapeutes : {elapsed:.2f}ms')

start = time.time()
class PsyMeetBestSite(ListView):
    model = PsyMeet
    context_object_name = _("psymeet")  # Utilisez gettext_lazy pour les contextes traduisibles
    template_name = "psy/recherche_therapeute.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['DEPARTEMENT_CHOICES'] = [
            (code, _(label)) for code, label in [
                ("01", "01 - Ain"),
                ("02", "02 - Aisne"),
                ("03", "03 - Allier"),
                ("04", "04 - Alpes-de-Haute-Provence"),
                ("05", "05 - Hautes-Alpes"),
                ("06", "06 - Alpes-Maritimes"),
                ("07", "07 - Ardèche"),
                ("08", "08 - Ardennes"),
                ("09", "09 - Ariège"),
                ("10", "10 - Aube"),
                ("11", "11 - Aude"),
                ("12", "12 - Aveyron"),
                ("13", "13 - Bouches-du-Rhône"),
                ("14", "14 - Calvados"),
                ("15", "15 - Cantal"),
                ("16", "16 - Charente"),
                ("17", "17 - Charente-Maritime"),
                ("18", "18 - Cher"),
                ("19", "19 - Corrèze"),
                ("21", "21 - Côte-d'Or"),
                ("22", "22 - Côtes-d'Armor"),
                ("23", "23 - Creuse"),
                ("24", "24 - Dordogne"),
                ("25", "25 - Doubs"),
                ("26", "26 - Drôme"),
                ("27", "27 - Eure"),
                ("28", "28 - Eure-et-Loir"),
                ("29", "29 - Finistère"),
                ("2A", "2A - Corse-du-Sud"),
                ("2B", "2B - Haute-Corse"),
                ("30", "30 - Gard"),
                ("31", "31 - Haute-Garonne"),
                ("32", "32 - Gers"),
                ("33", "33 - Gironde"),
                ("34", "34 - Hérault"),
                ("35", "35 - Ille-et-Vilaine"),
                ("36", "36 - Indre"),
                ("37", "37 - Indre-et-Loire"),
                ("38", "38 - Isère"),
                ("39", "39 - Jura"),
                ("40", "40 - Landes"),
                ("41", "41 - Loir-et-Cher"),
                ("42", "42 - Loire"),
                ("43", "43 - Haute-Loire"),
                ("44", "44 - Loire-Atlantique"),
                ("45", "45 - Loiret"),
                ("46", "46 - Lot"),
                ("47", "47 - Lot-et-Garonne"),
                ("48", "48 - Lozère"),
                ("49", "49 - Maine-et-Loire"),
                ("50", "50 - Manche"),
                ("51", "51 - Marne"),
                ("52", "52 - Haute-Marne"),
                ("53", "53 - Mayenne"),
                ("54", "54 - Meurthe-et-Moselle"),
                ("55", "55 - Meuse"),
                ("56", "56 - Morbihan"),
                ("57", "57 - Moselle"),
                ("58", "58 - Nièvre"),
                ("59", "59 - Nord"),
                ("60", "60 - Oise"),
                ("61", "61 - Orne"),
                ("62", "62 - Pas-de-Calais"),
                ("63", "63 - Puy-de-Dôme"),
                ("64", "64 - Pyrénées-Atlantiques"),
                ("65", "65 - Hautes-Pyrénées"),
                ("66", "66 - Pyrénées-Orientales"),
                ("67", "67 - Bas-Rhin"),
                ("68", "68 - Haut-Rhin"),
                ("69", "69 - Rhône"),
                ("70", "70 - Haute-Saône"),
                ("71", "71 - Saône-et-Loire"),
                ("72", "72 - Sarthe"),
                ("73", "73 - Savoie"),
                ("74", "74 - Haute-Savoie"),
                ("75", "75 - Paris"),
                ("76", "76 - Seine-Maritime"),
                ("77", "77 - Seine-et-Marne"),
                ("78", "78 - Yvelines"),
                ("79", "79 - Deux-Sèvres"),
                ("80", "80 - Somme"),
                ("81", "81 - Tarn"),
                ("82", "82 - Tarn-et-Garonne"),
                ("83", "83 - Var"),
                ("84", "84 - Vaucluse"),
                ("85", "85 - Vendée"),
                ("86", "86 - Vienne"),
                ("87", "87 - Haute-Vienne"),
                ("88", "88 - Vosges"),
                ("89", "89 - Yonne"),
                ("90", "90 - Territoire de Belfort"),
                ("91", "91 - Essonne"),
                ("92", "92 - Hauts-de-Seine"),
                ("93", "93 - Seine-Saint-Denis"),
                ("94", "94 - Val-de-Marne"),
                ("95", "95 - Val-d'Oise"),
                ("971", "971 - Guadeloupe"),
                ("972", "972 - Martinique"),
                ("973", "973 - Guyane"),
                ("974", "974 - La Réunion"),
                ("976", "976 - Mayotte")
            ]
        ]
        context['DIPLOME_CHOICES'] = [
            ("Diplômé d'état", _("Diplômé d'état")),
            ("Indépendant", _("Indépendant")),
        ]
        context['SPECIALITE_CHOICES'] = [
            ("Psychologie clinique", _("Psychologie clinique")),
            ("Psychologie du travail", _("Psychologie du travail")),
            ("Psychologie sociale", _("Psychologie sociale")),
        ]
        return context

    def get_queryset(self):
        start = time.time()
        queryset = super().get_queryset()

        departement = self.request.GET.get('departement')
        if departement:
            queryset = queryset.filter(departement=departement)

        diplome = self.request.GET.get('diplome')
        if diplome:
            queryset = queryset.filter(diplome=diplome)

        specialite = self.request.GET.get('specialite')
        if specialite:
            queryset = queryset.filter(specialite=specialite)

        # Filtrer par affiliation
        affiliation = self.request.GET.get('affiliation')
        if affiliation == 'true':
            queryset = queryset.filter(affiliation=True)
        elif affiliation == 'false':
            queryset = queryset.filter(affiliation=False)

        # Filtrer par émission de CO2
        co2 = self.request.GET.get('co2')
        if co2 == 'true':
            queryset = queryset.filter(co2=True)
        elif co2 == 'false':
            queryset = queryset.filter(co2=False)

        return queryset
end = time.time()
elapsed = end - start
print(f'Temps de recherche des sites des thérapeutes : {elapsed:.2f}ms')

class PsyHome(ListView):
    model = PsyMeet
    context_object_name = _("psys")  # Utilisez gettext_lazy pour les contextes traduisibles

@method_decorator(login_required, "dispatch")
class PsyCreate(CreateView):
    model = PsyMeet
    template_name = "psy/psy_create.html"
    fields = ['title', 'content', 'published']  # Optimisez les fields selon le models.py

@method_decorator(login_required, "dispatch")
class PsyUpdate(UpdateView):
    model = PsyMeet
    template_name = "psy/psy_edit.html"
    fields = ['title', 'content', 'published']  # Optimisez les fields selon le models.py

class PsyDetail(DetailView):
    model = PsyMeet
    context_object_name = _("psy")  # Utilisez gettext_lazy pour les contextes traduisibles
    template_name = "psy/psy_detail.html"
    fields = ['title', 'content', 'published']  # Optimisez les fields selon le models.py

@method_decorator(login_required, "dispatch")
class PsyDelete(DeleteView):
    model = PsyMeet
    success_url = reverse_lazy("psy_home")
