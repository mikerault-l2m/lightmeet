from django.contrib import admin
from blog.models import *

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'published')
    list_filter = ('published', 'category', 'date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
