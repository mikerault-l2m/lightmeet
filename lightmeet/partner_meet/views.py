from django.views.generic import TemplateView
from accounts.models import *
from django.shortcuts import render,redirect
from accounts.forms import *
from partner_meet.models import *
from partner_meet.forms import *
from django.conf import settings
import time
from django.contrib.auth.decorators import login_required

class Home(TemplateView):
    model = Lightener
    template_name = "partner_meet/Home.html"

class rencontrer(TemplateView):
    model = Lightener
    template_name = "partner_meet/Home_Rencontres.html"


@login_required

# Optimiser la class play_partner_meet, l'algorithme de recommandation de Lightmeet pour les sites de rencontre :

def play_partner_meet(request):
    if request.method == 'POST':
        form = PartnerMeetForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'partner_meet/Partner_Meet_Thanks_You.html')
    else:
        form = PartnerMeetForm()
    return render(request, 'partner_meet/Partner_Meet_Formulaire.html', {'form': form})

#

# from django.shortcuts import render
# from django.contrib import messages
# from .resources import SiteWebResource

# def import_data(request):
#     if request.method == 'POST':
#         resource = SiteWebResource()
#         dataset = Dataset()
#         new_data = request.FILES['myfile']

#         if not new_data.name.endswith('xls') and not new_data.name.endswith('xlsx'):
#             messages.error(request, 'Le fichier n\'est pas un fichier Excel')
#             return render(request, 'import_data.html')

#         imported_data = dataset.load(new_data.read(), format='xlsx')
#         result = resource.import_data(imported_data, dry_run=True)  # Dry run first to check if data is valid

#         if not result.has_errors():
#             resource.import_data(imported_data, dry_run=False)  # Import data again, this time for real
#             messages.success(request, 'Les données ont été importées avec succès')
#         else:
#             messages.error(request, 'Une erreur s\'est produite lors de l\'importation des données')

#     return render(request, 'import_data.html')




