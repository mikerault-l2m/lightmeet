from django.template import loader
from django.views.generic import TemplateView
from legal.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

# Pages de gestion des documents juridiques

class LegalDetail(DetailView):
    model = Legal
    context_object_name = "legal"
    template_name = "legal/legal_detail.html"
    fields = ['title', 'content', 'published']

@method_decorator(login_required, "dispatch")
class LegalCreate(CreateView):
    model = Legal
    template_name = "legal/legal_create.html"
    fields = ['title', 'content']
    # Ajout d'un verbose_name pour la classe
    verbose_name = _("Créer un document juridique")
    verbose_name_plural = _("Documents juridiques")

@method_decorator(login_required, "dispatch")
class LegalUpdate(UpdateView):
    model = Legal
    template_name = "legal/legal_edit.html"
    fields = ['title', 'content', 'published']
    # Ajout d'un verbose_name pour la classe
    verbose_name = _("Modifier un document juridique")
    verbose_name_plural = _("Documents juridiques")

@method_decorator(login_required, "dispatch")
class LegalDelete(DeleteView):
    model = Legal
    success_url = reverse_lazy("legal_home")
    # Ajout d'un verbose_name pour la classe
    verbose_name = _("Supprimer un document juridique")
    verbose_name_plural = _("Documents juridiques")

# Page de consentement, ML, PC et Politiques de Cookies

class LegalControlML(TemplateView):
    model = Legal
    template_name = "legal/ML.html"
    # Ajout d'un verbose_name pour la classe
    verbose_name = _("Politique de Mentions Légales")

class LegalControlCGU(TemplateView):
    model = Legal
    template_name = "legal/CGU.html"
    # Ajout d'un verbose_name pour la classe
    verbose_name = _("Conditions Générales d'Utilisation")

class LegalControlPDC(TemplateView):
    model = Legal
    template_name = "legal/PDC.html"
    # Ajout d'un verbose_name pour la classe
    verbose_name = _("Politique de Confidentialité")

class LegalControlPC(TemplateView):
    model = Legal
    template_name = "legal/PC.html"
    # Ajout d'un verbose_name pour la classe
    verbose_name = _("Politique de Cookies")

class LegalControlConsentement(TemplateView):
    model = Legal
    template_name = "partner_meet/Consentement.html"
    # Ajout d'un verbose_name pour la classe
    verbose_name = _("Consentement")
