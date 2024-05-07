from django.template import loader
from django.views.generic import TemplateView
from legal.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.template import loader
from django.views.generic import TemplateView
from legal.models import *

# Pages de gestion des documents juridiques

class LegalDetail(DetailView):
    model = Legal
    context_object_name = "legal"
    template_name = "legal/legal_detail.html"
    fields = ['title','content','published',]

@method_decorator(login_required,"dispatch")
class LegalCreate(CreateView):
    model = Legal
    template_name = "legal/legal_create.html"
    fields = ['title','content',]

@method_decorator(login_required,"dispatch")
class LegalUpdate(UpdateView):
    model = Legal
    template_name = "legal/legal_edit.html"
    fields = ['title','content','published',]

@method_decorator(login_required,"dispatch")
class LegalDelete(DeleteView):
    model = Legal
    success_url = reverse_lazy("legal_home")


# Page de consentement, ML, PC et Politiques de Cookies

class legal_Control_ML(TemplateView):
    model = Legal
    template_name = "legal/ML.html"

class legal_Control_CGU(TemplateView):
    model = Legal
    template_name = "legal/CGU.html"

class legal_Control_PDC(TemplateView):
    model = Legal
    template_name = "legal/PDC.html"

class legal_Control_PC(TemplateView):
    model = Legal
    template_name = "legal/PC.html"

class legal_Control_Consentement(TemplateView):
    model = Legal
    template_name = "partner_meet/Consentement.html"