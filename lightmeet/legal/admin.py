from django.contrib import admin
from legal.models import *

class LegalAdmin(admin.ModelAdmin):
    # Define how Legal model should be displayed in admin
    pass

admin.site.register(legal_Controler,LegalAdmin)

