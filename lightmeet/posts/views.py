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

#1er article
class BlogPost1(TemplateView):
    template_name = "posts/First_Article.html"

#2nd article
class BlogPost2(TemplateView):
    template_name = "posts/Second_Article.html"

    def get_queryset(self):
        return BlogPost.objects.all().select_related('author')


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



