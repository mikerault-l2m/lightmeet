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

# Etape 1 : Lancement de la page principale Lightmeet :
start = time.time()

class Home(TemplateView):
    model = Lightener
    template_name = 'partner_meet/Home.html'

end = time.time()
elapsed = end - start
print(f"Temps d'affichage de LightMeet : {elapsed:.2f}ms")

# Etape 2 : Création du statut de visiteur avec récupération de l'adresse IP et de la localisation :
start = time.time()

def enregistrer_visiteur(request):
    # Détecter la langue de l'utilisateur
    user_language = get_language_from_request(request)
    # Activer la langue pour cette requête
    activate(user_language)

    form = LightenerCreationForm(request.POST)
    if request.method == "POST":
        ip_address = get_client_ip(request)
        location = get_location(ip_address)
        Visitor.objects.create(ip_address=ip_address, location=location)

    # Récupérer les articles de blog et traduire les titres dynamiquement
    posts = BlogPost.objects.all()
    for post in posts:
        post.title = _(post.title)  # Traduire dynamiquement le titre en fonction de la langue active

    return render(request, "partner_meet/Home.html", {"form": form, "posts": posts})

# A: Récupération de l'adresse IP :
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# B: Récupération de la localisation
def get_location(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        if data['status'] == 'success':
            location = f"{data['city']}, {data['country']}"
        else:
            location = "Unknown"
    except Exception as e:
        location = "Unknown"
    return location

end = time.time()
elapsed = end - start
print(f"Temps de récupération adresse IP et location sur LightMeet : {elapsed:.2f}ms")

start = time.time()

class PartnerMeetHome(ListView):
    model = PartnerMeet
    context_object_name = "partnermeet"
    template_name = "partner_meet/partnermeet_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CATEGORIE_CHOICES'] = (
            ("Généraliste", "Site généraliste"),
            ("Libertin", "Site libertin"),
            ("Senior", "Site senior"),
            ("Religieux", "Site religieux"),
            ("Haut-de-gamme", "Site haut-de-gamme"),
        )
        context['RELATION_CHOICES'] = (
            ('Durables', 'Durables'),
            ('Homosexuelles', 'Homosexuelles'),
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

        # Filtrer par affiliation
        affiliation = self.request.GET.get('affiliation')
        if affiliation == 'true':
            queryset = queryset.filter(affiliation=True)
        elif affiliation == 'false':
            queryset = queryset.filter(affiliation=False)

        # Filtre selon la émission de CO2
        co2 = self.request.GET.get('co2')
        if co2 == 'true':
            queryset = queryset.filter(co2=True)
        elif co2 == 'false':
            queryset = queryset.filter(co2=False)

        # Filtrer par description (recherche partielle)
        description = self.request.GET.get('description')
        if description:
            queryset = queryset.filter(description__icontains=description)

        # Traduire dynamiquement la description pour chaque partenaire
        for partner in queryset:
            partner.description = _(partner.description)

        return queryset

class PartnerMeetBestSite(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CATEGORIE_CHOICES'] = (
            ("Généraliste", "Site généraliste"),
            ("Libertin", "Site libertin"),
            ("Senior", "Site senior"),
            ("Religieux", "Site religieux"),
            ("Haut-de-gamme", "Site haut-de-gamme"),
        )
        context['RELATION_CHOICES'] = (
            ('Durables', 'Durables'),
            ('Homosexuelles', 'Homosexuelles'),
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

        # Filtre selon la émission de CO2
        co2 = self.request.GET.get('co2')
        if co2 == 'true':
            queryset = queryset.filter(co2=True)
        elif co2 == 'false':
            queryset = queryset.filter(co2=False)

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