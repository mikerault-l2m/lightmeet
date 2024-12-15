from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _  # Importez gettext_lazy pour les chaînes traduisibles
from support.models import SupportTicket
from support.forms import SupportTicketForm
from django.shortcuts import render

class ContactSubscribe(TemplateView):
    model = SupportTicket
    template_name = ("support/base_Support.html")  # Utilisez gettext_lazy ici pour les chemins de template

class ContactSubscribe_2(TemplateView):
    model = SupportTicket
    template_name = ("support/Support.html")  # Utilisez gettext_lazy ici pour les chemins de template

class ContactSubscribe_3(TemplateView):
    model = SupportTicket
    template_name = ("support/Thanks.html")  # Utilisez gettext_lazy ici pour les chemins de template

def SupportContact(request):
    if request.method == "POST":
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, ("support/Thanks.html"), context={"form": form})  # Utilisez gettext_lazy ici pour le chemin du template
    else:
        form = SupportTicketForm()
    return render(request, ("support/Support.html"), context={"form": form})  # Utilisez gettext_lazy ici pour le chemin du template
