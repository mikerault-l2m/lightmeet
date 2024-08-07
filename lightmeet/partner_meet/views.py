from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import *
from accounts.models import *
from accounts.forms import *
from partner_meet.models import *
from partner_meet.forms import *
from posts.models import *
from posts.views import *
from legal.models import *
from django.conf import settings
import time
from django.db.models import F, ExpressionWrapper, DecimalField
from decimal import Decimal
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.utils.translation import gettext as _

# Etape 1 : Lancement de la page principale Lightmeet :

start = time.time()
class Home(TemplateView):
    model = Lightener
    template_name = 'partner_meet/Home.html'

end = time.time()
elapsed = end - start
print(f'Temps d\'affichage de LightMeet : {elapsed:.2}ms')



######## Etape 2 : Création du statut de visiteur avec récupération de l'adresse IP et de la localisation :
start = time.time()

def enregistrer_visiteur(request):
    form = LightenerCreationForm(request.POST)
    if request.method == "POST":
        ip_address = get_client_ip(request)
        location = get_location(ip_address)
        Visitor.objects.create(ip_address=ip_address, location=location)
        posts = BlogPost.objects.all()
        return render(request, "partner_meet/Home.html", {"form": form, "posts": posts})
    return render(request, "partner_meet/Home.html", {"form": form, "posts": posts})


# A: Récupération de l'adresse IP :
def get_client_ip(request):
    # Si l'en-tête HTTP_X_FORWARDED_FOR est présent, récupère la première adresse IP de la liste
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        # Sinon, récupère l'adresse IP directe du client depuis REMOTE_ADDR
        ip = request.META.get('REMOTE_ADDR')
    return ip

# B: Récupération de la localisation
def get_location(ip):
    try:
        # Envoie une requête à l'API ip-api.com pour obtenir la localisation basée sur l'adresse IP fournie
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        if data['status'] == 'success':
            # Si la requête est réussie, extrait la ville et le pays de la réponse JSON
            location = f"{data['city']}, {data['country']}"
        else:
            # Si la requête échoue, déclare la localisation comme "Unknown"
            location = "Unknown"
    except Exception as e:
        # En cas d'exception, déclare la localisation comme "Unknown"
        location = "Unknown"
    return location

end = time.time()
elapsed = end - start
print(f'Temps de récupération adresse IP et location sur LightMeet : {elapsed:.2f}ms')




start = time.time()
class PartnerMeetHome(ListView):
    model = PartnerMeet
    context_object_name = "partnermeet"
    template_name = "partner_meet/partnermeet_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CATEGORIE_CHOICES'] = (
            ("Généraliste", _("Site généraliste")),
            ("Senior",_("Site senior")),
            ("Haut-de-gamme", _("Site haut-de-gamme")),
        )
        context['RELATION_CHOICES'] = (
            ('Durables', _("Durables")),
            ('Homosexuelles', _('Homosexuelles')),
        )
        context['AGE_CHOICES'] = (
            ('18-30', '18-30 '),
            ('31-45', '31-45 '),
            ('+ 46', '+ 46'),
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        # Trier par affiliation (si disponible)
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'ranking':
            queryset = queryset.order_by('-ranking')


        return queryset
end = time.time()
elapsed = end - start
print(f'Temps d\'affichage des critères des sites de rencontre : {elapsed:.2}ms')

start = time.time()
class PartnerMeetBestSite(ListView):
    model = PartnerMeet
    context_object_name = "partnermeet"
    template_name = "partner_meet/recherche_rencontre.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CATEGORIE_CHOICES'] = (
            ("Généraliste", _("Site généraliste")),
            ("Senior", _("Site senior")),
            ("Haut-de-gamme", _("Site haut-de-gamme")),
        )
        context['RELATION_CHOICES'] = (
            ('Durables', _('Durables')),
            ('Homosexuelles', _('Homosexuelles')),
        )
        context['AGE_CHOICES'] = (
            ('18-30', '18-30 '),
            ('31-45', '31-45 '),
            ('+ 46', '+ 46'),
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

       # Trier par ranking (si disponible)
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'ranking':
            queryset = queryset.order_by('ranking')

        return queryset
end = time.time()
elapsed = end - start
print(f'Temps de recherche des sites de rencontre : {elapsed:.2}ms')


# Cette méthode  correspond aux filtrage selon les demandes des clients.
#
#    def get_queryset(self):
#        queryset = super().get_queryset()
#
#        # Filtrer en fonction des préférences de l'utilisateur si nécessaire
#        categorie = self.request.GET.get('categorie')
#        relation =  self.request.GET.get('relation')
#        age = self.request.GET.get('age')
#
#        if categorie:
#            queryset = queryset.filter(categorie=categorie)
#        if relation:
#            queryset = queryset.filter(relation=relation)
#        if age:
#            if age == 'plus':
#                queryset = queryset.filter(age__gte=55)
#           else:
#                lower_age, upper_age = age.split('-')
#                queryset = queryset.filter(age__gte=lower_age, age__lte=upper_age)

#        # Calculer les scores pour chaque objet PartnerMeet
#        for partner in queryset:
#            partner.score = self.calculer_score(partner)

#        return queryset

#    def calculer_score(self, partner):
#        # Calcul du score pour le partenaire en fonction de ses attributs
#        score = Decimal('0')
#        POIDS_PRIX = Decimal('0.5')
#        POIDS_VISITEURS = Decimal('0.5')
#
#        # Calcul de la différence de prix entre le partenaire et les autres partenaires
#        difference_prix = F('prix_avg') - partner.prix_avg
#
#        # Calcul de la différence du nombre de visiteurs par mois entre le partenaire et les autres partenaires
#        difference_visiteurs = F('Visites_France') - partner.Visites_France
#
#        # Calcul du score en fonction des différences de prix et de visiteurs par mois
#        score += POIDS_PRIX * difference_prix
#       score += POIDS_VISITEURS * difference_visiteurs
#
#        return score

# end = time.time()
# elapsed = end - start
# print(f'Temps de filtrage des sites de rencontre : {elapsed:.2}ms')

# Réalise cette étape d'optimisation lors du clic sur recherche par l'utilisateur
class PartnerMeetDetail(DetailView):
    model = PartnerMeet
    context_object_name = "site"
    template_name = "partner_meet/partner_meet_detail.html"

# Step create site de rencontres :
@method_decorator(login_required, name='dispatch')
class PartnerMeetCreate(CreateView):
    model = PartnerMeet
    template_name = "partner_meet/partner_meet_create.html"
    fields = ['nom', 'url', 'logo', 'genre_find', 'age']

#Step edit site de rencontres:
@method_decorator(login_required, name='dispatch')
class PartnerMeetUpdate(UpdateView):
    model = PartnerMeet
    template_name = "partner_meet/partner_meet_edit.html"
    fields = ['nom', 'url', 'logo', 'genre_find', 'age']

#Step delete site de rencontres :
@method_decorator(login_required, name='dispatch')
class PartnerMeetDelete(DeleteView):
    model = PartnerMeet
    success_url = reverse_lazy("partner_meet_list")

#Ici peut-être faut il changer certaines variables pour adapter au models PartnerMeetHome

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