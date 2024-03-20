from django.views.generic import ListView
from posts.models import *

class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"
