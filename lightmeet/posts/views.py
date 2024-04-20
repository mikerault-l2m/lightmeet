from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy
from posts.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

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