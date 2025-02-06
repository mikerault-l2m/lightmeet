from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy
from posts.models import BlogPost
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _

# Menu déroulant

class BlogPostHome(ListView):
    model = BlogPost
    context_object_name = "posts"  # C'est ce que vous utiliserez dans le modèle
    template_name = "posts/blogpost_list.html"

    def get_queryset(self):
        return BlogPost.objects.all()  # Récupérer tous les articles de blog

from django.views.generic import TemplateView

# 1er article
class BlogPost1(TemplateView):
    template_name = "posts/First_Article.html"

# 2ème article
class BlogPost2(TemplateView):
    template_name = "posts/Second_Article.html"

    def get_queryset(self):
        return BlogPost.objects.all().select_related('author')

# 3ème article
class BlogPost3(TemplateView):
    template_name = "posts/Third_Article.html"

# 4ème article
class BlogPost4(TemplateView):
    template_name = "posts/Fourth_Article.html"

# 5ème article
class BlogPost5(TemplateView):
    template_name = "posts/Fifth_Article.html"

# 6ème article
class BlogPost6(TemplateView):
    template_name = "posts/Sixth_Article.html"

# 7ème article
class BlogPost7(TemplateView):
    template_name = "posts/Seventh_Article.html"

# 8ème article
class BlogPost8(TemplateView):
    template_name = "posts/Eighth_Article.html"

# 9ème article
class BlogPost9(TemplateView):
    template_name = "posts/Ninth_Article.html"

# 10ème article
class BlogPost10(TemplateView):
    template_name = "posts/Tenth_Article.html"

# 11ème article
class BlogPost11(TemplateView):
    template_name = "posts/Eleventh_Article.html"

# 12ème article
class BlogPost12(TemplateView):
    template_name = "posts/Twelfth_Article.html"

# 13ème article
class BlogPost13(TemplateView):
    template_name = "posts/Thirteenth_Article.html"

# 14ème article
class BlogPost14(TemplateView):
    template_name = "posts/Fourteenth_Article.html"






class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"
    template_name = "posts/blogpost_detail.html"
    fields = ['title', 'content', 'published']

    # La méthode `blog_detail` n'est pas nécessaire dans une classe `DetailView`.
    # Utilisez `get_object` ou surchargez les méthodes `get_context_data` pour des besoins spécifiques.


class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title', 'content']

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['label_suffix'] = ''  # Suffix vide
        return kwargs


class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = ['title', 'content', 'published']

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['label_suffix'] = ''  # Suffix vide
        return kwargs


class BlogPostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog_home")



