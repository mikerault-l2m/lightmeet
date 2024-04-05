from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import *
from accounts.forms import *
from partner_meet.models import *
from partner_meet.forms import *
from django.conf import settings
import time


class Home(TemplateView):
    model = Lightener
    template_name = "partner_meet/Home.html"

class rencontrer(TemplateView):
    model = Lightener
    template_name = "partner_meet/Home_Rencontres.html"


class Recherche_Meet(TemplateView):
    template_name = "partner_meet/Partner_Meet_Formulaire.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        meet_sites = Comparateur.objects.all()

        genre_choices = (
            ("Homme", "Je cherche un homme"),
            ("Femme", "Je cherche une femme"),
            ("Non déterminé", "Je cherche tout le monde"),
        )
        relation_choices = (
            ('durables', 'Durables'),
            ('Relation d\'un soir', 'Relation d\' un soir'),
            ('toutes', 'Toutes')
        )
        age_choices = (
            ('18-25', '18-25 ans'),
            ('25-35', '25-35 ans'),
            ('35-45', '35-45 ans'),
            ('45-55', '45-55 ans'),
            ('plus', 'Plus de 55 ans')
        )

        meet_sites_data = []
        for meet_site in meet_sites:
            meet_site_data = {
                'nom': meet_site.nom,
                'genre_find': meet_site.genre_find,
                'logo': meet_site.logo,
                'url': meet_site.url,
                'relation': meet_site.relation,
                'age': meet_site.age,
            }
            meet_sites_data.append(meet_site_data)

        context['meet_sites'] = meet_sites_data
        context['genre_choices'] = genre_choices
        context['relation_choices'] = relation_choices
        context['age_choices'] = age_choices

        return context


# Step 1 : Il faut d'abord que la version avec Genre,Relation et Age fonctionne avant d'aller chercher les meilleures sites !

#Step 2 : On utilise List Detail Create Update et Delete pour faire apparaitre nos marques

#class PartnerMeetHome(ListView):
#    model = Comparateur
#    context_object_name = "posts"

#    def get_queryset(self):
#        queryset = super().get_queryset()

#class PartnerMeetDetail(DetailView):
#    model = Comparateur
#    context_object_name = "site"
#    template_name = "partner_meet/partner_meet_detail.html"


#@method_decorator(login_required, name='dispatch')
#class PartnerMeetCreate(CreateView):
#    model = Comparateur
#    template_name = "partner_meet/partner_meet_create.html"
#    fields = ['nom', 'url', 'logo', 'genre_find', 'relation', 'age']

#@method_decorator(login_required, name='dispatch')
#class PartnerMeetUpdate(UpdateView):
#    model = Comparateur
#    template_name = "partner_meet/partner_meet_edit.html"
#    fields = ['nom', 'url', 'logo', 'genre_find', 'relation', 'age']

#@method_decorator(login_required, name='dispatch')
#class PartnerMeetDelete(DeleteView):
#    model = Comparateur
#    success_url = reverse_lazy("partner_meet_list")





def trouver_meilleur_site(site_comparateur, sites):
    meilleur_site = None
    meilleur_score = -1

    # Parcourez les sites pour trouver le meilleur site
    for site in sites:
        if site != site_comparateur:  # Ne pas comparer un site avec lui-même
            score = calculer_score(site_comparateur, site)
            if score > meilleur_score:
                meilleur_site = site
                meilleur_score = score
    return meilleur_site


def calculer_score(site1, site2):
    # Poids des différents critères de comparaison
    poids_popularite = 0.5
    poids_prix = 0.3
    poids_fonctionnalites = 0.2

    # Calcul du score en fonction des attributs des sites et de leur importance respective
    score = 0

    # Comparaison de la popularité
    score += poids_popularite * abs(site1.popularite - site2.popularite)

    # Comparaison du prix
    score += poids_prix * abs(site1.prix - site2.prix)

    # Comparaison des fonctionnalités (par exemple, longueur de la liste)
    score += poids_fonctionnalites * abs(len(site1.fonctionnalites) - len(site2.fonctionnalites))

    return score


@login_required
class meet_compare(TemplateView):
    model = Lightener
    template_name = "partner_meet/meet_comparer.html"


@login_required

# Optimiser la class play_partner_meet, l'algorithme de recommandation de Lightmeet pour les sites de rencontre :

def play_partner_meet(request):
    if request.method == 'POST':
        form = PartnerMeetForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'partner_meet/Partner_Meet_Thanks_You.html')
    else:
        form = PartnerMeetForm()
    return render(request, 'partner_meet/Partner_Meet_Formulaire.html', {'form': form})

#

# from django.shortcuts import render
# from django.contrib import messages
# from .resources import SiteWebResource

# def import_data(request):
#     if request.method == 'POST':
#         resource = SiteWebResource()
#         dataset = Dataset()
#         new_data = request.FILES['myfile']

#         if not new_data.name.endswith('xls') and not new_data.name.endswith('xlsx'):
#             messages.error(request, 'Le fichier n\'est pas un fichier Excel')
#             return render(request, 'import_data.html')

#         imported_data = dataset.load(new_data.read(), format='xlsx')
#         result = resource.import_data(imported_data, dry_run=True)  # Dry run first to check if data is valid

#         if not result.has_errors():
#             resource.import_data(imported_data, dry_run=False)  # Import data again, this time for real
#             messages.success(request, 'Les données ont été importées avec succès')
#         else:
#             messages.error(request, 'Une erreur s\'est produite lors de l\'importation des données')

#     return render(request, 'import_data.html')




