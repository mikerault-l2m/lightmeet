from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class BlogPost(models.Model):
    image = models.FileField(upload_to='images_blog/', default='', verbose_name="Image")
    url = models.URLField(max_length=200, blank=True, verbose_name="URL")
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    hashtag = models.CharField(max_length=255, unique=True, verbose_name="Hashtag")
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="Slug")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Auteur")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")
    created_on = models.DateField(blank=True, null=True, verbose_name="Date de création")
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")
    description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog_home")

