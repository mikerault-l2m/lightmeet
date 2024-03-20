from django.contrib import admin
from support.models import *

class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('sender_email', 'subject', 'created_at')
    search_fields = ('sender_email', 'subject')
    readonly_fields = ('created_at',)

admin.site.register(SupportTicket, SupportTicketAdmin)
