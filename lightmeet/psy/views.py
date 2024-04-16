from django.views.generic import TemplateView
from django.shortcuts import render
from django.conf import settings
import time
from psy.models import *

class psy_Home(TemplateView):
    model = PsyMeet
    template_name = "psy/Home_Psy.html"

class psy_recherche(TemplateView):
    model = PsyMeet
    template_name = "psy/Home_Psy.html"