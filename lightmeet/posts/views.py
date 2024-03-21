from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from django.urls import reverse_lazy
from posts.models import *

class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title','content',]

class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields = ['title','content','published',]

class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "posts"
    template_name = "posts/blogpost_detail.html"
    fields = ['title','content','published',]

class BlogPostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog")