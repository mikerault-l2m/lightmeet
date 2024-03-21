from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse

User = get_user_model()

class BlogPost(models.Model):
    title = models.CharField(max_length=255,unique=True,verbose_name="Titre")
    slug = models.SlugField(max_length=255,unique=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True,null=True)
    published = models.BooleanField(default=False,verbose_name="Publié")
    content = models.TextField(blank=True,verbose_name="Contenu")
    description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = "Notre Article"
        verbose_name_plural = "Nos Articles"
        ordering=["-created_on"]


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("blog_home")

