from django.db import models

class PsyMeet(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    localisation = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100, blank=True)
    specialite = models.CharField(max_length=100)
    anciennete = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='psy_images/', blank=True)
    site_web = models.URLField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.specialite}"

    class Meta:
        verbose_name = "Notre thérapeute professionnel"
        verbose_name_plural = "Nos thérapeutes professionnels"