from django.db import models
# Bug du serveur : il faut d'abord créer l'API avec 'python manage.py startapp import_export'
#from import_export.models import resources


class PartnerMeet(models.Model):
    nom = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='MeetSites/', null=True, blank=True)
    url = models.URLField(blank=True) # URL de redirection du site web a associé à la variable a 'affiliation' - 1 - Site
    nombre_visiteurs_par_mois = models.CharField(max_length=100)# - 3 Membres - # Cette variable comptabilise tous les 3 mois le nombre de visiteur du site web.

    CATEGORIE_CHOICES = (
    ("Généraliste", "Je cherche un site généraliste"),
    ("Libertin", "Je cherche un site libertin"),
    ("Non déterminé", "Je cherche tout le monde"),
    ("Senior","Je cherche un site pour senior"),
    ("Extra-conjugales","Je cherche un site extra-conjugal"),
    ("Tchat","Je cherche un tchat instantané"),
    ("Haut-de-gamme","Je cherche un site haut-de-gamme"),
    ("Religion","Je cherche un site soutenant une religion"),
    ("Handicap","Je cherche un site à destination du handicap"),
    ("Locale","Je cherche un site locale"),
    ("Insolite","Je cherche un site insolite"),
    ("Géolocalisation","Je cherche un site axé sur la géolocalisation")
)
    categorie = models.CharField(choices=CATEGORIE_CHOICES, max_length=25, default='Non déterminé')

    pourcent_femmes_choices = (
    ("absence de femmes", "Absence de femmes"),
    ("bas", "Bas"),
    ('moyen', 'Moyen'),
    ('élevé', 'Élevé'),
    ('integral', 'Intégral'),
)
    pourcent_femmes = models.CharField(max_length=50, choices=pourcent_femmes_choices)


    AGE_CHOICES = (
        ('18-25', '18-25 ans'),
        ('25-35', '25-35 ans'),
        ('35-45', '35-45 ans'),
        ('45-55', '45-55 ans'),
        ('plus', 'Plus de 55 ans')
    )
    age = models.CharField(max_length=50, choices=AGE_CHOICES)



    prix_avg = models.DecimalField(max_digits=10, decimal_places=2, default=0) # 2 Points forts : Prix

    google_trustpilot_avg = models.FloatField(null=True, blank=True) # 4 - Note Utilisateur
    affiliation = models.BooleanField(default=False)# 5 - Sélection cocher # Ce partenaire est affilié à la société Listen2Meet par un contrat d'affiliation.

    description = models.TextField(null=True, blank=True) # Courte description du site de rencontres - 2 - Points forts en quelques mots
    ranking = models.PositiveIntegerField(null=True, blank=True) # Ce numéro positionne la variable selon l'algo de pertinence.
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ranking} - {self.nom}"

    class Meta:
        verbose_name = "Notre site de rencontre partenaire"
        verbose_name_plural = "Nos sites de rencontres partenaires"


