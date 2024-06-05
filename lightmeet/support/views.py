from django.views.generic import TemplateView
from support.models import *
from django.conf import settings
from django.shortcuts import render
from support.forms import *
import time

class ContactSubscribe(TemplateView):
    model = SupportTicket
    template_name = "support/base_Support.html"

class ContactSubscribe_2(TemplateView):
    model = SupportTicket
    template_name = "support/Support.html"

class ContactSubscribe_3(TemplateView):
    model = SupportTicket
    template_name = "support/Thanks.html"

# Temps pour la transmission du message de l'utilisateur :
start = time.time()

def SupportContact(request):
        if request.method == "POST":
            form = SupportTicketForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'support/Thanks.html',context={"form": form})
        else:
            form = SupportTicketForm()
        return render(request, "support/Support.html", context={"form": form})

end = time.time()
elapsed = end - start
print(f'Temps d\'exécution du transfert des mails : {elapsed:.2}ms')


