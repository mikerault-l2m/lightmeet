from django.contrib import admin
from legal.models import *

class LegalAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'last_updated', 'created_on', 'published']

admin.site.register(Legal)

