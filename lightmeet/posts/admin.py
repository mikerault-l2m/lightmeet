from django.contrib import admin
from posts.models import *

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'last_updated')
    list_editable = ('published',)  # Ajoutez ici les champs que vous souhaitez rendre éditables
    list_filter = ('published', 'author')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_on'
    readonly_fields = ('last_updated',)

admin.site.register(BlogPost, BlogPostAdmin)
