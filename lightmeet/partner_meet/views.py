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
from legal.models import *
from django.conf import settings
import time
from django.db.models import F
from decimal import Decimal
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

# Etape 1 : Lancement de la page principale Lightmeet :

start = time.time()
class Home(TemplateView):
    model = Lightener
    template_name = 'partner_meet/Home.html'

end = time.time()
elapsed = end - start
print(f'Temps d\'affichage de LightMeet : {elapsed:.2f}ms')

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
            location = _("Unknown")
    except Exception as e:
        location = _("Unknown")
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
            ("Senior", _("Site senior")),
            ("Haut-de-gamme", _("Site haut-de-gamme")),
        )
        context['RELATION_CHOICES'] = (
            ('Durables', _("Durables")),
            ('Homosexuelles', _("Homosexuelles")),
        )
        context['AGE_CHOICES'] = (
            ('18-30', ("18-30")),
            ('31-45', ("31-45")),
            ('+ 46', ("+ 46")),
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'ranking':
            queryset = queryset.order_by('-ranking')
        return queryset

end = time.time()
elapsed = end - start
print(f'Temps d\'affichage des critères des sites de rencontre : {elapsed:.2f}ms')

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
            ('Durables', _("Durables")),
            ('Homosexuelles', _("Homosexuelles")),
        )
        context['AGE_CHOICES'] = (
            ('18-30', ("18-30")),
            ('31-45', ("31-45")),
            ('+ 46', ("+ 46")),
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'ranking':
            queryset = queryset.order_by('ranking')
        return queryset

end = time.time()
elapsed = end - start
print(f'Temps de recherche des sites de rencontre : {elapsed:.2f}ms')

class PartnerMeetDetail(DetailView):
    model = PartnerMeet
    context_object_name = "site"
    template_name = "partner_meet/partner_meet_detail.html"

@method_decorator(login_required, name='dispatch')
class PartnerMeetCreate(CreateView):
    model = PartnerMeet
    template_name = "partner_meet/partner_meet_create.html"
    fields = ['nom', 'url', 'logo', 'genre_find', 'age']
    # Ajout d'un verbose_name pour la classe
    verbose_name = _("Créer un site de rencontre")

@method_decorator(login_required, name='dispatch')
class PartnerMeetUpdate(UpdateView):
    model = PartnerMeet
    template_name = "partner_meet/partner_meet_edit.html"
    fields = ['nom', 'url', 'logo', 'genre_find', 'age']
    # Ajout d'un verbose_name pour la classe
    verbose_name = _("Modifier un site de rencontre")

@method_decorator(login_required, name='dispatch')
class PartnerMeetDelete(DeleteView):
    model = PartnerMeet
    success_url = reverse_lazy("partner_meet_list")
    # Ajout d'un verbose_name pour la classe
    verbose_name = _("Supprimer un site de rencontre")

def trouver_meilleur_site(site_comparateur, sites):
    meilleur_site = None
    meilleur_score = -1
    for site in sites:
        if site != site_comparateur:
            score = calculer_score(site_comparateur, site)
            if score > meilleur_score:
                meilleur_site = site
                meilleur_score = score
    return meilleur_site

def calculer_score(site1, site2):
    poids_popularite = 0.5
    poids_prix = 0.3
    poids_fonctionnalites = 0.2
    score = 0
    score += poids_popularite * abs(site1.popularite - site2.popularite)
    score += poids_prix * abs(site1.prix - site2.prix)
    score += poids_fonctionnalites * abs(len(site1.fonctionnalites) - len(site2.fonctionnalites))
    return score
