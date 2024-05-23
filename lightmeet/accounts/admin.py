from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from accounts.models import *

class LightenerAdmin(admin.ModelAdmin):
    list_display = ('email', 'prenom', 'is_active', 'is_staff', 'is_admin','ip_address', 'location')
    search_fields = ('email', 'prenom')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Lightener, LightenerAdmin)

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'location', 'timestamp')
    search_fields = ('ip_address', 'location')
    list_filter = ('timestamp',)

admin.site.register(Visitor, VisitorAdmin)