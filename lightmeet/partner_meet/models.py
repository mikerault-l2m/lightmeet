from django.db import models
# Bug du serveur : il faut d'abord créer l'API avec 'python manage.py startapp import_export'
#from import_export.models import resources


class PartnerMeet(models.Model):
    nom = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='MeetSites/', null=True, blank=True)  # Champ pour le logo du site: 200*200
    url = models.URLField(blank=True) # URL de redirection du site web a associé à la variable a 'affiliation'
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

    prix_avg = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    innovation = models.TextField(null=True, blank=True) # Mise en valeur de la marque.

    ranking = models.PositiveIntegerField(null=True, blank=True) # Ce numéro positionne la variable selon l'algo de pertinence.

    affiliation = models.BooleanField(default=False) # Ce partenaire est affilié à la société Listen2Meet par un contrat d'affiliation.
    categorie = models.CharField(max_length=100) # Ceci corresponds à la catégorie du site web.


    nombre_visiteurs_par_mois = models.PositiveIntegerField() # Cette variable comptabilise tous les 3 mois le nombre de visiteur du site web.

    pourcentage_femmes = models.FloatField(null=True, blank=True) # PROBLEME : Cet indicateur indique aux célibataires recherchant des femmes le % de femmes présente sur le site.
    tranche_age = models.CharField(max_length=50) # BIAIS D'ECHANTILLONAGE : Pourcentage de la tranche d'âge majoritaire sur la plateforme.
    google_trustpilot_avg = models.FloatField(null=True, blank=True) # BIAIS D'ECHANTILLONAGE :

    description = models.TextField(null=True, blank=True) # Courte description du site de rencontres

    #storytelling_comment = models.TextField(null=True, blank=True) # Le remmplissage de cet indicateur reste complexe et chronophage.

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ranking} - {self.description}"

    class Meta:
        verbose_name = "Notre site de rencontre partenaire"
        verbose_name_plural = "Nos sites de rencontres partenaires"


