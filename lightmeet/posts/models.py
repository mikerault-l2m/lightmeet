from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class BlogPost(models.Model):
    image = models.FileField(upload_to='images_blog/', default='', verbose_name=_("Image"))
    title = models.CharField(max_length=255, unique=True, verbose_name=_("Titre"))
    hashtag = models.CharField(max_length=255, unique=True, verbose_name=_("Hashtag"))
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name=_("Slug"))
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Auteur"))
    last_updated = models.DateTimeField(auto_now=True, verbose_name=_("Dernière mise à jour"))
    created_on = models.DateField(blank=True, null=True, verbose_name=_("Date de création"))
    published = models.BooleanField(default=False, verbose_name=_("Publié"))
    content = models.TextField(blank=True, verbose_name=_("Contenu"))
    description = models.TextField(verbose_name=_("Description"))

    #comment = models.CharField(default=False,max_length=500,verbose_name=_("Commentaire"))
    #like = models.BooleanField(default=False,verbose_name=_("Liké"))

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog_home")
