from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from accounts.models import *

class LightenerAdmin(admin.ModelAdmin):
    list_display = ('email', 'prenom', 'is_active', 'is_staff', 'is_admin')
    search_fields = ('email', 'prenom')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Lightener, LightenerAdmin)