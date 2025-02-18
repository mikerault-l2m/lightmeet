from django.db import models
from django.utils.translation import gettext_lazy as _
# Bug du serveur : il faut d'abord créer l'API avec 'python manage.py startapp import_export'
#from import_export.models import resources

class PartnerMeet(models.Model):
    nom = models.CharField(max_length=100)
    LOGO = models.ImageField(upload_to='MeetSites/', null=True, blank=True)
    url = models.URLField(blank=True) # URL de redirection du site web associé à la variable 'affiliation'
    Visites = models.CharField(max_length=100) # - 3 Membres - # Cette variable comptabilise tous les 3 mois le nombre de visiteurs du site web.
    FLAG = models.ImageField(upload_to='Countries/', null=True, blank=True)
    CATEGORIE_CHOICES = (
            ("Généraliste", "Site généraliste"),
            ("Senior", "Site senior"),
            ("Haut-de-gamme", "Site haut-de-gamme"),
    )
    categorie = models.CharField(choices=CATEGORIE_CHOICES, max_length=25, default='Généraliste')
    RELATION_CHOICES = (
        #('Toutes','Toutes'),
            ('Durables', 'Durables'),
            ('Amicales', 'Amicales'),
            ('LGBTQ+','LGBTQ+'),
    )
    relation = models.CharField(choices=RELATION_CHOICES, max_length=25, default='Toutes')


    # Version adulte
    CATEGORIE_CHOICE = (
            ("Jeune", "Site pour jeunes"),
            ("Géolocalisation", "Géolocalisation"),
            ("Interculturelles", "Interculturelles"),
            ("Femme ronde","Femme ronde"),
            ("Discrétion","Discrétion"),

    )
    categories = models.CharField(choices=CATEGORIE_CHOICE, max_length=25, default='Géolocalisation')

    RELATION_CHOICE = (
        #('Toutes','Toutes'),
            ('Adultère', 'Adultère'),
            ('Lesbienne', 'Lesbienne'),
            ('Gay','Gay'),
            ('Interculturelles','Interculturelles'),
    )
    relations = models.CharField(choices=RELATION_CHOICE, max_length=25, default='Toutes')

    AGE_CHOICES = (
            ('18-30', '18-30 '),
            ('31-45', '31-45 '),
            ('+ 46', '+ 46'),
    )
    age = models.CharField(max_length=50, choices=AGE_CHOICES)

    COUNTRY = (
        ('France','FRA'),
        ('Australia','AUS'),
        ('United States','USA'),
        ('Belgium','BEL'),
        ('United Kingdom','UK'),
        ('Canada','CAN')
    )
    countries = models.CharField(choices=COUNTRY, max_length=25, default='France')
    prix_avg = models.DecimalField(max_digits=10, decimal_places=2, default=0) # 2 Points forts : Prix
    trustpilot = models.FloatField(null=True, blank=True) # 4 - Note Utilisateur
    affiliation = models.BooleanField(default=False) # 5 - Sélection cocher # Ce partenaire est affilié à la société Listen2Meet par un contrat d'affiliation.
    affiliation_adulte = models.BooleanField(default=False)
    free = models.BooleanField(default=False)
    co2 = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True) # Courte description du site de rencontres - 2 - Points forts en quelques mots
    ranking = models.PositiveIntegerField(null=True, blank=True) # Ce numéro positionne la variable selon l'algo de pertinence.
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ranking} - {self.nom} || {self.countries} || {self.affiliation_adulte}"
    class Meta:
        verbose_name = "Notre site de rencontre partenaire"
        verbose_name_plural = "Nos sites de rencontres partenaires"