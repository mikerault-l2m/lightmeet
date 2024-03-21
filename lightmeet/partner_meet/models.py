from django.db import models
from import_export import resources
# Insérer les variables décidées sur Miro

class PartnerMeet(models.Model):
    numero = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)  # Champ pour le logo du site
    url = models.URLField()
    non_affilie = models.BooleanField(default=False)
    categorie = models.CharField(max_length=100)
    nombre_visiteurs_par_mois = models.IntegerField()
    pourcentage_femmes = models.FloatField()
    tranche_age = models.CharField(max_length=50)
    durabilite = models.CharField(max_length=50)
    qualite_du_site = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    ranking = models.PositiveIntegerField()
    partner_logo = models.ImageField(upload_to='partner_logos/')
    google_trustpilot_avg = models.FloatField()
    description = models.TextField()
    ideal_age = models.CharField(max_length=50)
    daily_visits = models.PositiveIntegerField()
    innovation_features = models.CharField(max_length=255)
    trustpilot_reviews = models.PositiveIntegerField()
    audience_profile = models.TextField()
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    storytelling_comment = models.TextField()
    site_web = models.URLField(blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    gender_percentage = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.ranking} - {self.description}"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Notre site de rencontre partenaire"
        verbose_name_plural = "Nos sites de rencontres partenaires"

class PartnerMeetResource(resources.ModelResource):
    class Meta:
        model = PartnerMeet