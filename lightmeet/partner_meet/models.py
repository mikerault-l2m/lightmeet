from django.db import models
from django.utils.translation import gettext_lazy as _

class PartnerMeet(models.Model):
    nom = models.CharField(max_length=100, verbose_name=("Nom"))
    logo = models.ImageField(upload_to='MeetSites/', null=True, blank=True, verbose_name=("Logo"))
    url = models.URLField(blank=True, help_text=("URL de redirection vers le site web associé à l'affiliation"), verbose_name=_("URL"))
    visites_france = models.CharField(max_length=100, help_text=("Nombre de visiteurs du site web en France, mis à jour tous les 3 mois."), verbose_name=_("Visites France"))

    CATEGORIE_CHOICES = (
        ("Généraliste", _("Site généraliste")),
        ("Senior", _("Site senior")),
        ("Haut-de-gamme", _("Site haut de gamme")),
    )
    categorie = models.CharField(choices=CATEGORIE_CHOICES, max_length=25, default='Généraliste', verbose_name=_("Catégorie"))

    RELATION_CHOICES = (
        ('Durables', _('Relations durables')),
        ('Homosexuelles', _('Relations homosexuelles')),
    )
    relation = models.CharField(choices=RELATION_CHOICES, max_length=25, default='Durables', verbose_name=_("Relation"))

    AGE_CHOICES = (
        ('18-30', '18-30'),
        ('31-45', '31-45'),
        ('46+', '46+'),
    )
    age = models.CharField(max_length=50, choices=AGE_CHOICES, verbose_name=_("Âge"))

    prix_avg = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text=_("Prix moyen des services proposés."), verbose_name=_("Prix moyen"))

    trustpilot = models.FloatField(null=True, blank=True, help_text=_("Note utilisateur sur Trustpilot."), verbose_name=_("Note Trustpilot"))

    affiliation = models.BooleanField(default=False, help_text=_("Indique si le partenaire est affilié à Listen2Meet par un contrat d'affiliation."), verbose_name=_("Affiliation"))

    free = models.BooleanField(default=False, help_text=_("Indique si le service est gratuit."), verbose_name=_("Gratuit"))

    co2 = models.BooleanField(default=False, help_text=_("Indique si le site est respectueux de l'environnement."), verbose_name=_("Respect de l'environnement"))

    description = models.TextField(null=True, blank=True, help_text=_("Courte description du site de rencontres."), verbose_name=_("Description"))

    ranking = models.PositiveIntegerField(null=True, blank=True, help_text=_("Position du site selon l'algorithme de pertinence."), verbose_name=_("Classement"))

    date_creation = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))

    def __str__(self):
        return f"{self.ranking or ''} - {self.nom}"

    class Meta:
        verbose_name = _("Site de rencontre partenaire")
        verbose_name_plural = _("Sites de rencontres partenaires")
