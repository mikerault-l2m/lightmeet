from django.db import models
# Bug du serveur : il faut d'abord créer l'API avec 'python manage.py startapp import_export'
#from import_export.models import resources

# Insérer les variables décidées sur Miro

# Votre autre code Django pour gérer la logique de votre application


class Comparateur(models.Model):
    nom = models.CharField(max_length=100)
    url = models.URLField()
    logo = models.ImageField(upload_to='MeetSites/', null=True, blank=True)  # Champ pour le logo du site
    GENRE_FIND_CHOICES = (
        ("Homme", "Je cherche un homme"),
        ("Femme", "Je cherche une femme"),
        ("Non déterminé", "Je cherche tout le monde"),
    )
    genre_find = models.CharField(choices=GENRE_FIND_CHOICES, max_length=25, default='Non déterminé')
    RELATION_CHOICES = (
        ('durables', 'Durables'),
        ('Relation d\'un soir', 'Relation d\' un soir'),
        ('toutes', 'Toutes')
    )
    relation = models.CharField(max_length=50, choices=RELATION_CHOICES)
    AGE_CHOICES = (
        ('18-25', '18-25 ans'),
        ('25-35', '25-35 ans'),
        ('35-45', '35-45 ans'),
        ('45-55', '45-55 ans'),
        ('plus', 'Plus de 55 ans')
    )
    age = models.CharField(max_length=50, choices=AGE_CHOICES)
    popularite = models.PositiveIntegerField(default=0, null=True)  # Rendre le champ populaire facultatif
    prix = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fonctionnalites = models.TextField(default='')
    def __str__(self):
        return f"{self.nom} - {self.url}"

    class Meta:
        verbose_name = "Notre marque de rencontre partenaire"
        verbose_name_plural = "Nos marques de rencontres partenaires"






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


# class ComparateurSiteRencontre(models.Model):
#     nom = models.CharField(max_length=100)
#     url = models.URLField()
#     logo = models.ImageField(upload_to='Logos/', null=True, blank=True)  # Champ pour le logo du site
#     genre = models.CharField(max_length=50, choices=(('femmes', 'Femmes'), ('hommes', 'Hommes'), ('tous', 'Tous')))
#     relation = models.CharField(max_length=50, choices=(('durables', 'Durables'), ('Relation d''un soir', 'Relation d'' un soir'), ('toutes', 'Toutes')))
#     age = models.CharField(max_length=50, choices=(('18-25', '18-25 ans'), ('25-35', '25-35 ans'), ('35-45', '35-45 ans'), ('45-55', '45-55 ans'), ('plus', 'Plus de 55 ans')))
#     popularite = models.PositiveIntegerField(default=0)
#     prix = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     fonctionnalites = models.TextField(default='')

#     def __str__(self):
#         return self.nom

#     class Meta:
#         verbose_name = "Notre marque de rencontre partenaire"
#         verbose_name_plural = "Nos marques de rencontres partenaires"

# PartnerMeetResource(resources.ModelResource):
#    class Meta:
#        model = PartnerMeet