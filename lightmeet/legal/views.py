from django.template import loader
from django.views.generic import TemplateView
from legal.models import legal_Controler

class legal_Control_2(TemplateView):
    model = legal_Controler
    template_name = "legal/Légal_2.html"

class legal_Control_CGU(TemplateView):
    model = legal_Controler
    template_name = "legal/CGU.html"

class legal_Control_PDC(TemplateView):
    model = legal_Controler
    template_name = "legal/PDC.html"

class legal_Control_PC(TemplateView):
    model = legal_Controler
    template_name = "legal/PC.html"

