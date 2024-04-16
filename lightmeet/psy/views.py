from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings
import time
from psy.models import *
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy
from posts.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class PsyHome(ListView):
    model = PsyMeet
    context_object_name = "psys"

@method_decorator(login_required,"dispatch")
class PsyCreate(CreateView):
    model = PsyMeet
    template_name = "psy/psy_create.html"
    fields = ['title','content','published',]# Optimise les fields selon le models.py

@method_decorator(login_required,"dispatch")
class PsyUpdate(UpdateView):
    model = PsyMeet
    template_name = "psy/psy_edit.html"
    fields = ['title','content','published',] # Optimise les fields selon le models.py

class PsyDetail(DetailView):
    model = PsyMeet
    context_object_name = "psy"
    template_name = "psy/psy_detail.html"
    fields = ['title','content','published',] # Optimise les fields selon le models.py

@method_decorator(login_required,"dispatch")
class PsyDelete(DeleteView):
    model = PsyMeet
    success_url = reverse_lazy("psy_home")