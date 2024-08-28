from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Legal(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name=_("Titre"))
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Auteur"))
    last_updated = models.DateTimeField(auto_now=True, verbose_name=_("Dernière mise à jour"))
    created_on = models.DateField(auto_now_add=True, verbose_name=_("Date de création"))  # Modifié pour auto-remplir lors de la création
    published = models.BooleanField(default=False, verbose_name=_("Publié"))
    content = models.TextField(blank=True, verbose_name=_("Contenu"))
    description = models.TextField(verbose_name=_("Description"))

    class Meta:
        verbose_name = _("Document juridique")
        verbose_name_plural = _("Documents juridiques")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("legal_home")
