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
from django.db.models import Q

# Affichage de la page principale :

class Home(TemplateView):
    model = Lightener
    template_name = "partner_meet/Home.html"

start = time.time()
class PartnerMeetHome(ListView):
    model = Comparateur
    context_object_name = "partner_meet"

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtrer en fonction des choix de l'utilisateur
        gender = self.request.GET.get('gender')
        relationship = self.request.GET.get('relationship')
        age_range = self.request.GET.get('age_range')

        if gender:
            queryset = queryset.filter(genre=gender)
        if relationship:
            queryset = queryset.filter(relation=relationship)
        if age_range:
            if age_range == 'plus':
                queryset = queryset.filter(age__gte=55)
            else:
                lower_age, upper_age = age_range.split('-')
                queryset = queryset.filter(age__gte=lower_age, age__lte=upper_age)

        if not self.request.user.is_authenticated:
            queryset = queryset.filter(published=True)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Choix pour l'utilisateur : genre, type de relation et tranche d'âge
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

        context['genre_choices'] = genre_choices
        context['relation_choices'] = relation_choices
        context['age_choices'] = age_choices

        return context



end = time.time()
elapsed = end - start
print(f'Temps d\'exécution de la recherche de sites de rencontres : {elapsed:.2f} secondes')


# Réalise cette étape d'optimisation lors du clic sur recherche par l'utilisateur
class PartnerMeetDetail(DetailView):
    model = Comparateur
    context_object_name = "site"
    template_name = "partner_meet/partner_meet_detail.html"

# Step create site de rencontres :
@method_decorator(login_required, name='dispatch')
class PartnerMeetCreate(CreateView):
    model = Comparateur
    template_name = "partner_meet/partner_meet_create.html"
    fields = ['nom', 'url', 'logo', 'genre_find', 'relation', 'age']

#Step edit site de rencontres:
@method_decorator(login_required, name='dispatch')
class PartnerMeetUpdate(UpdateView):
    model = Comparateur
    template_name = "partner_meet/partner_meet_edit.html"
    fields = ['nom', 'url', 'logo', 'genre_find', 'relation', 'age']

#Step delete site de rencontres :
@method_decorator(login_required, name='dispatch')
class PartnerMeetDelete(DeleteView):
    model = Comparateur
    success_url = reverse_lazy("partner_meet_list")





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




