from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy
from posts.models import BlogPost
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.core.paginator import Paginator

class BlogArticles(ListView):
    model = BlogPost
    context_object_name = "posts"  # Context name is not a translatable string
    template_name = "posts/blogpost_articles.html"

class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"  # Context name is not a translatable string
    template_name = "posts/blogpost_detail.html"
    fields = ['title', 'content', 'published']

class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title', 'content']

    # Adding verbose_name for translatable field labels
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['label_suffix'] = _('')  # Add this if you have labels with suffix
        return kwargs

class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = ['title', 'content', 'published']

    # Adding verbose_name for translatable field labels
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['label_suffix'] = _('')  # Add this if you have labels with suffix
        return kwargs

class BlogPostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog_home")

class BlogPost1(TemplateView):
    model = BlogPost
    template_name = "posts/First_Article.html"

    def get_queryset(self):
        return BlogPost.objects.all().select_related('author')
