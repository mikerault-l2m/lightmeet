from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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
from django.http import HttpResponse
import requests  # Ensure you import requests since you are using it in get_location
from django.utils.translation import activate, get_language_from_request, gettext as _ #pour la langue
from django.views.generic import ListView
from .models import PartnerMeet  # Assurez-vous que vous importez le bon modèle.
from django.shortcuts import render
from django.http import HttpRequest
from django.utils.translation import get_language
# Etape 1 : Lancement de la page principale Lightmeet :
start = time.time()

class Home(TemplateView):
    model = Lightener
    template_name = 'partner_meet/Home.html'

end = time.time()
elapsed = end - start
print(f"Temps d'affichage de LightMeet : {elapsed:.2f}ms")




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


#C - Affichage du drapeau par pays

def determine_flag(request):
    flags = {
        "fr": "France",
        "fr-be": "Belgium",
        "en-us": "United States",
        "en-gb": "United Kingdom",
        "en-au": "Australia",
        "de": "Germany",
        "da": "Denmark",
        "pt": "Portugal",
        "nl": "Netherlands",
        "es": "Spain",
    }
    return flags.get(get_language(), "default")

def partnermeet_list(request):
    flag = determine_flag(request)
    # Tu pourrais également récupérer d'autres données ici si nécessaire
    return render(request, 'partnermeet_list.html', {'flag': flag})


## Version tout public
import time
from django.conf import settings
from django.shortcuts import render
from django.utils.translation import get_language
from django.views.generic import ListView
from .models import PartnerMeet

start = time.time()

class PartnerMeetListView(ListView):
    model = PartnerMeet
    context_object_name = "partners"
    template_name = "partner_meet/partnermeet_list.html"

    def determine_flag(self, request):
        """
        Fonction pour déterminer le pays en fonction de la langue.
        """
        flags = {
            "fr": "France",
            "fr-be": "Belgium",
            "en-us": "United States",
            "en-gb": "United Kingdom",
            "en-au": "Australia",
            "de": "Germany",
            "da": "Denmark",
            "pt": "Portugal",
            "nl": "Netherlands",
            "es": "Spain",
        }
        return flags.get(get_language(), "default")

    def get_context_data(self, **kwargs):
        """
        Ajouter des données supplémentaires au contexte du template, comme le flag et MEDIA_URL.
        """
        context = super().get_context_data(**kwargs)
        context['flag'] = self.determine_flag(self.request)
        context['MEDIA_URL'] = settings.MEDIA_URL  # Ajout de MEDIA_URL au contexte
        return context

    def get_queryset(self):
        """
        Retourne les partenaires filtrés en fonction de la langue extraite de l'URL.
        """
        queryset = super().get_queryset()

        # Extraction optimisée de la langue dans l'URL
        lang_code = self.kwargs.get('lang') or self.request.path.split('/')[1]

        # Gestion uniquement de 'fr' et 'en-us'
        language_country_map = {
            'fr': "France",
            'en-us': "United States",
            'fr-be': "Belgium",
        }

        country = language_country_map.get(lang_code)

        if country:
            queryset = queryset.filter(countries=country)

        return queryset.order_by("-ranking")  # Tri par ranking pour optimiser l'affichage

end = time.time()
elapsed = end - start
print(f"Temps de recherche des sites de rencontre : {elapsed:.2f}ms")


start = time.time()
class PartnerMeetHome(ListView):
    model = PartnerMeet
    context_object_name = "partnermeet"
    template_name = "partner_meet/partnermeet_list.html"

    def PartnerMeetHome(request):
        selected_country = ["France", "German", "United States"]  # Exemple : cette valeur pourrait provenir de l'URL ou d'une autre logique
        countries = ["France", "German", "United States"]

        return render(request, 'partner_meet/partnermeet_list.html', {
            'selected_country': selected_country,
            'countries': countries
        })


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CATEGORIE_CHOICES'] = (
            ("Généraliste", "Site généraliste"),
            ("Senior", "Site senior"),
            ("Haut-de-gamme", "Site haut-de-gamme"),
        )

        context['COUNTRY'] = (
            ('France','FRA'),
            ('Australia','AUS'),
            ('United States','USA'),
            ('United Kingdom','UK'),
            ('Belgium','BEL'),
            ('Canada','CAN'),
        )

        context['RELATION_CHOICES'] = (
            ('Durables', 'Durables'),
            ('Amicales', 'Amicales'),
            ('LGBTQ+','LGBTQ+'),
        )
        context['AGE_CHOICES'] = (
            ('18-30', '18-30'),
            ('31-45', '31-45'),
            ('+ 46', '+ 46'),
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtrer par âge
        age = self.request.GET.get('age')
        if age:
            queryset = queryset.filter(age=age)

        # Filtrer par prix moyen
        prix_avg = self.request.GET.get('prix_avg')
        if prix_avg:
            queryset = queryset.filter(prix_avg=prix_avg)

        # Trier par affiliation (si disponible)
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'affiliation':
            queryset = queryset.order_by('affiliation')

        # Trier par trustpilot (si disponible)
        if sort_by == 'trustpilot':
            queryset = queryset.order_by('-trustpilot')

        # Filtrer par description (recherche partielle)
        description = self.request.GET.get('description')
        if description:
            queryset = queryset.filter(description__icontains=description)

        # Traduire dynamiquement la description pour chaque partenaire
        for partner in queryset:
            partner.description = _(partner.description)

        return queryset
class PartnerMeetBestSite(ListView):
    model = PartnerMeet  # Définissez ici le modèle associé à la vue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CATEGORIE_CHOICES'] = (
            ("Généraliste", "Site généraliste"),
            ("Senior", "Site senior"),
            ("Haut-de-gamme", "Site haut-de-gamme"),
        )
        context['COUNTRY'] = (
            ('France','FRA'),
            ('Australia','AUS'),
            ('United States','USA'),
            ('United Kingdom','UK'),
            ('Belgium','BEL'),
            ('Canada','CAN'),
        )
        context['RELATION_CHOICES'] = (
            ('Durables', 'Durables'),
            ('LGBTQ+', 'LGBTQ+'),
        )
        context['AGE_CHOICES'] = (
            ('18-30', '18-30'),
            ('31-45', '31-45'),
            ('+ 46', '+ 46'),
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()


        # Filtrer par âge
        age = self.request.GET.get('age')
        if age:
            queryset = queryset.filter(age=age)

        # Filtrer par prix moyen
        prix_avg = self.request.GET.get('prix_avg')
        if prix_avg:
            queryset = queryset.filter(prix_avg=prix_avg)

        # Trier par trustpilot (si disponible)
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'trustpilot':
            queryset = queryset.order_by('-trustpilot')

        # Filtrer par affiliation
        affiliation = self.request.GET.get('affiliation')
        if affiliation == 'true':
            queryset = queryset.filter(affiliation=True)
        elif affiliation == 'false':
            queryset = queryset.filter(affiliation=False)

        # Filtre selon la gratuité
        free = self.request.GET.get('free')
        if free == 'true':
            queryset = queryset.filter(free=True)
        elif free == 'false':
            queryset = queryset.filter(free=False)

        # Filtrer par description (recherche partielle)
        description = self.request.GET.get('description')
        if description:
            queryset = queryset.filter(description__icontains=description)

        # Filtrer par catégorie
        categorie = self.request.GET.get('categorie')
        if categorie:
            queryset = queryset.filter(categorie=categorie)

        # Trier par ranking (si disponible)
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'ranking':
            queryset = queryset.order_by('ranking')

        return queryset
end = time.time()
elapsed = end - start
print(f"Temps de recherche des sites de rencontre : {elapsed:.2f}ms")

# Version adulte

start = time.time()
class PartnerMeetListView(ListView):
    model = PartnerMeet
    context_object_name = "partners"
    template_name = "partner_meet/partnermeet_list_adulte.html"

    def get_queryset(self):
        """
        Retourne les partenaires filtrés en fonction de la langue extraite de l'URL.
        """
        queryset = super().get_queryset()

        # Extraction optimisée de la langue dans l'URL
        lang_code = self.kwargs.get('lang') or self.request.path.split('/')[1]

        # Gestion uniquement de 'fr' et 'en-us'
        language_country_map = {
            'fr': "France",
            'en-us': "United States"
        }

        country = language_country_map.get(lang_code)

        if country:
            queryset = queryset.filter(countries=country)

        return queryset.order_by("-ranking")
      # Tri par ranking pour optimiser l'affichage
end = time.time()
elapsed = end - start
print(f"Temps de recherche des sites de rencontre : {elapsed:.2f}ms")


start = time.time()
class PartnerMeetHome_Adulte(ListView):
    model = PartnerMeet
    context_object_name = "partnermeet"
    template_name = "partner_meet/partnermeet_list_adulte.html"

    def PartnerMeetHome(request):
        selected_country = "France"  # Exemple : cette valeur pourrait provenir de l'URL ou d'une autre logique
        countries = ["France", "German", "United States"]

        return render(request, 'partner_meet/partnermeet_list.html', {
            'selected_country': selected_country,
            'countries': countries
        })


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CATEGORIE_CHOICE'] = (
            ("Jeune", "Site pour jeunes"),
            ("Géolocalisation", "Géolocalisation"),
            ("Interculturelles", "Site interculturelles"),
            ("Femme ronde","Femme ronde"),
            ("Discrétion","Discrétion"),
        )
        context['COUNTRY'] = (
            ('France','FRA'),
            ('Australia','AUS'),
            ('United States','USA'),
            ('United Kingdom','UK'),
            ('Belgium','BEL'),
            ('Canada','CAN'),
        )

        context['RELATION_CHOICE'] = (
            ('Adultère', 'Adultère'),
            ('Lesbienne', 'Lesbienne'),
            ('Gay','Gay'),
            ('Interculturelles'),
        )
        context['AGE_CHOICES'] = (
            ('18-30', '18-30'),
            ('31-45', '31-45'),
            ('+ 46', '+ 46'),
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtrer par âge
        age = self.request.GET.get('age')
        if age:
            queryset = queryset.filter(age=age)

        # Filtrer par prix moyen
        prix_avg = self.request.GET.get('prix_avg')
        if prix_avg:
            queryset = queryset.filter(prix_avg=prix_avg)

        # Trier par affiliation_adulte (si disponible)
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'affiliation_adulte':
            queryset = queryset.order_by('affiliation_adulte')

        # Trier par trustpilot (si disponible)
        if sort_by == 'trustpilot':
            queryset = queryset.order_by('-trustpilot')

        # Filtrer par description (recherche partielle)
        description = self.request.GET.get('description')
        if description:
            queryset = queryset.filter(description__icontains=description)

        # Traduire dynamiquement la description pour chaque partenaire
        for partner in queryset:
            partner.description = _(partner.description)

        return queryset
class PartnerMeetBestSite_Adulte(ListView):
    model = PartnerMeet  # Définissez ici le modèle associé à la vue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CATEGORIE_CHOICES'] = (
            ("Généraliste", "Site généraliste"),
            ("Senior", "Site senior"),
            ("Haut-de-gamme", "Site haut-de-gamme"),
        )
        context['COUNTRY'] = (
            ('France','FRA'),
            ('Australia','AUS'),
            ('United States','USA'),
            ('United Kingdom','UK'),
            ('Belgium','BEL'),
            ('Canada','CAN'),
        )
        context['RELATION_CHOICES'] = (
            ('Durables', 'Durables'),
            ('LGBTQ+', 'LGBTQ+'),
        )
        context['AGE_CHOICES'] = (
            ('18-30', '18-30'),
            ('31-45', '31-45'),
            ('+ 46', '+ 46'),
        )
        return context

    def get_queryset(self):
        """
        Retourne les partenaires filtrés en fonction de la langue extraite de l'URL.
        """
        queryset = super().get_queryset()

        # Extraction optimisée de la langue dans l'URL
        lang_code = self.kwargs.get('lang') or self.request.path.split('/')[1]

        # Gestion uniquement de 'fr' et 'en-us'
        language_country_map = {
            'fr': "France",
            'en-us': "United States"
        }

        country = language_country_map.get(lang_code)

        if country:
            queryset = queryset.filter(countries=country)

        return queryset.order_by("-ranking")
      # Tri par ranking pour optimiser l'affichage
end = time.time()
elapsed = end - start
print(f"Temps de recherche des sites de rencontre : {elapsed:.2f}ms")


start = time.time()
class PartnerMeetHome_Adulte(ListView):
    model = PartnerMeet
    context_object_name = "partnermeet"
    template_name = "partner_meet/partnermeet_list_adulte.html"

    def PartnerMeetHome(request):
        selected_country = "France"  # Exemple : cette valeur pourrait provenir de l'URL ou d'une autre logique
        countries = ["France", "German", "United States"]

        return render(request, 'partner_meet/partnermeet_list.html', {
            'selected_country': selected_country,
            'countries': countries
        })


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CATEGORIE_CHOICE'] = (
            ("Jeune", "Site pour jeunes"),
            ("Géolocalisation", "Géolocalisation"),
            ("Interculturelles", "Site interculturelles"),
            ("Femme ronde","Femme ronde"),
            ("Discrétion","Discrétion"),
        )
        context['COUNTRY'] = (
            ('France','FRA'),
            ('Australia','AUS'),
            ('United States','USA'),
            ('United Kingdom','UK'),
            ('Belgium','BEL'),
            ('Canada','CAN'),
        )

        context['RELATION_CHOICE'] = (
            ('Adultère', 'Adultère'),
            ('Lesbienne', 'Lesbienne'),
            ('Gay','Gay'),
            ('Interculturelles'),
        )
        context['AGE_CHOICES'] = (
            ('18-30', '18-30'),
            ('31-45', '31-45'),
            ('+ 46', '+ 46'),
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtrer par âge
        age = self.request.GET.get('age')
        if age:
            queryset = queryset.filter(age=age)

        # Filtrer par prix moyen
        prix_avg = self.request.GET.get('prix_avg')
        if prix_avg:
            queryset = queryset.filter(prix_avg=prix_avg)

        # Trier par affiliation_adulte (si disponible)
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'affiliation_adulte':
            queryset = queryset.order_by('affiliation_adulte')

        # Trier par trustpilot (si disponible)
        if sort_by == 'trustpilot':
            queryset = queryset.order_by('-trustpilot')

        # Filtrer par description (recherche partielle)
        description = self.request.GET.get('description')
        if description:
            queryset = queryset.filter(description__icontains=description)

        # Traduire dynamiquement la description pour chaque partenaire
        for partner in queryset:
            partner.description = _(partner.description)

        return queryset
end = time.time()
elapsed = end - start
print(f"Temps de recherche des sites de rencontre : {elapsed:.2f}ms")

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
#def trouver_meilleur_site(site_comparateur, sites):
#    meilleur_site = None
#    meilleur_score = -1
#    # Parcourez les sites pour trouver le meilleur site
#    for site in sites:
#        if site != site_comparateur:  # Ne pas comparer un site avec lui-même
#            score = calculer_score(site_comparateur, site)
#            if score > meilleur_score:
#                meilleur_site = site
#                meilleur_score = score
#    return meilleur_site
#def calculer_score(site1, site2):
#    # Poids des différents critères de comparaison
#    poids_popularite = 0.5
#    poids_prix = 0.3
#    poids_fonctionnalites = 0.2
#    # Calcul du score en fonction des attributs des sites et de leur importance respective
#    score = 0
#    # Comparaison de la popularité
#    score += poids_popularite * abs(site1.popularite - site2.popularite)
#    # Comparaison du prix
#    score += poids_prix * abs(site1.prix - site2.prix)
#    # Comparaison des fonctionnalités (par exemple, longueur de la liste)
#    score += poids_fonctionnalites * abs(len(site1.fonctionnalites) - len(site2.fonctionnalites))
#    return score