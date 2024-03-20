from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.conf import settings
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    content = models.TextField()
    description = models.TextField()

    class Meta:
        verbose_name = "Notre Article"
        verbose_name_plural = "Nos Articles"
        ordering=["-date","-published"]


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog-post", kwargs={"slug": self.slug})
