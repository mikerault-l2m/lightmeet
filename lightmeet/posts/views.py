from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy
from posts.models import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

class BlogArticles(ListView):
    model = BlogPost
    context_object_name = "posts"  # Use underscores instead of hyphens
    template_name = "posts/blogpost_articles.html"

    def get_queryset(self):
        return BlogPost.objects.all().select_related('author')

@method_decorator(login_required,"dispatch")
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title','content',]

@method_decorator(login_required,"dispatch")
class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = ['title','content','published',]

class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"
    template_name = "posts/blogpost_detail.html"
    fields = ['title','content','published',]

@method_decorator(login_required,"dispatch")
class BlogPostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog_home")