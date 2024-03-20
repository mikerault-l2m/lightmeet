from django.views.generic import TemplateView
from support.models import *
from django.shortcuts import render
from support.forms import *
from django.conf import settings
import time

class SupportModel(TemplateView):
    model = SupportTicket
    template_name = "support/Contact.html"