from django.contrib import admin
from posts.models import *

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'published')
    list_filter = ('published', 'author')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_on'
    readonly_fields = ('last_updated',)

admin.site.register(BlogPost, BlogPostAdmin)
