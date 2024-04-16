from django.db import models
# Bug du serveur : il faut d'abord créer l'API avec 'python manage.py startapp import_export'
#from import_export.models import resources


class PartnerMeet(models.Model):
    nom = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='MeetSites/', null=True, blank=True)
    GENRE_FIND_CHOICES = (
        ("Homme", "Je cherche un homme"),
        ("Femme", "Je cherche une femme"),
        ("Non déterminé", "Je cherche tout le monde"),
    )
    genre_find = models.CharField(choices=GENRE_FIND_CHOICES, max_length=25, default='Non déterminé')
    categorie = models.CharField(max_length=100, null=True, blank=True)
    RELATION_CHOICES = (
        ('durables', 'Durables'),
        ('Relation d\'un sois', 'Relation d\' un sois'),
        ('gays','Gays'),
        ('lesbiennes','Lesbiennes'),
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

    url = models.URLField(blank=True) # URL de redirection du site web a associé à la variable a 'affiliation' - 1 - Site
    description = models.TextField(null=True, blank=True) # Courte description du site de rencontres - 2 - Points forts en quelques mots
    prix_avg = models.DecimalField(max_digits=10, decimal_places=2, default=0) # 2 Points forts : Prix
    tranche_age = models.CharField(max_length=50) # 3 Membres - # BIAIS D'ECHANTILLONAGE : Pourcentage de la tranche d'âge majoritaire sur la plateforme.
    nombre_visiteurs_par_mois = models.CharField(max_length=100)# - 3 Membres - # Cette variable comptabilise tous les 3 mois le nombre de visiteur du site web.
    google_trustpilot_avg = models.FloatField(null=True, blank=True) # 4 - Note Utilisateur
    affiliation = models.BooleanField(default=False)# 5 - Sélection cocher # Ce partenaire est affilié à la société Listen2Meet par un contrat d'affiliation.

    ranking = models.PositiveIntegerField(null=True, blank=True) # Ce numéro positionne la variable selon l'algo de pertinence.

    pourcentage_femmes = models.FloatField(null=True, blank=True) # PROBLEME : Cet indicateur indique aux célibataires recherchant des femmes le % de femmes présente sur le site.

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ranking} - {self.description}"

    class Meta:
        verbose_name = "Notre site de rencontre partenaire"
        verbose_name_plural = "Nos sites de rencontres partenaires"


