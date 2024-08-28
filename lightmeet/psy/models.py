from django.db import models
from django.utils.translation import gettext_lazy as _

class PsyMeet(models.Model):

    # Critère 1 - Choix des départements par des tuples (valeur, libellé)
    DEPARTEMENT_CHOICES = (
        ("01", _("01 - Ain")),
        ("02", _("02 - Aisne")),
        ("03", _("03 - Allier")),
        ("04", _("04 - Alpes-de-Haute-Provence")),
        ("05", _("05 - Hautes-Alpes")),
        ("06", _("06 - Alpes-Maritimes")),
        ("07", _("07 - Ardèche")),
        ("08", _("08 - Ardennes")),
        ("09", _("09 - Ariège")),
        ("10", _("10 - Aube")),
        ("11", _("11 - Aude")),
        ("12", _("12 - Aveyron")),
        ("13", _("13 - Bouches-du-Rhône")),
        ("14", _("14 - Calvados")),
        ("15", _("15 - Cantal")),
        ("16", _("16 - Charente")),
        ("17", _("17 - Charente-Maritime")),
        ("18", _("18 - Cher")),
        ("19", _("19 - Corrèze")),
        ("21", _("21 - Côte-d'Or")),
        ("22", _("22 - Côtes-d'Armor")),
        ("23", _("23 - Creuse")),
        ("24", _("24 - Dordogne")),
        ("25", _("25 - Doubs")),
        ("26", _("26 - Drôme")),
        ("27", _("27 - Eure")),
        ("28", _("28 - Eure-et-Loir")),
        ("29", _("29 - Finistère")),
        ("2A", _("2A - Corse-du-Sud")),
        ("2B", _("2B - Haute-Corse")),
        ("30", _("30 - Gard")),
        ("31", _("31 - Haute-Garonne")),
        ("32", _("32 - Gers")),
        ("33", _("33 - Gironde")),
        ("34", _("34 - Hérault")),
        ("35", _("35 - Ille-et-Vilaine")),
        ("36", _("36 - Indre")),
        ("37", _("37 - Indre-et-Loire")),
        ("38", _("38 - Isère")),
        ("39", _("39 - Jura")),
        ("40", _("40 - Landes")),
        ("41", _("41 - Loir-et-Cher")),
        ("42", _("42 - Loire")),
        ("43", _("43 - Haute-Loire")),
        ("44", _("44 - Loire-Atlantique")),
        ("45", _("45 - Loiret")),
        ("46", _("46 - Lot")),
        ("47", _("47 - Lot-et-Garonne")),
        ("48", _("48 - Lozère")),
        ("49", _("49 - Maine-et-Loire")),
        ("50", _("50 - Manche")),
        ("51", _("51 - Marne")),
        ("52", _("52 - Haute-Marne")),
        ("53", _("53 - Mayenne")),
        ("54", _("54 - Meurthe-et-Moselle")),
        ("55", _("55 - Meuse")),
        ("56", _("56 - Morbihan")),
        ("57", _("57 - Moselle")),
        ("58", _("58 - Nièvre")),
        ("59", _("59 - Nord")),
        ("60", _("60 - Oise")),
        ("61", _("61 - Orne")),
        ("62", _("62 - Pas-de-Calais")),
        ("63", _("63 - Puy-de-Dôme")),
        ("64", _("64 - Pyrénées-Atlantiques")),
        ("65", _("65 - Hautes-Pyrénées")),
        ("66", _("66 - Pyrénées-Orientales")),
        ("67", _("67 - Bas-Rhin")),
        ("68", _("68 - Haut-Rhin")),
        ("69", _("69 - Rhône")),
        ("70", _("70 - Haute-Saône")),
        ("71", _("71 - Saône-et-Loire")),
        ("72", _("72 - Sarthe")),
        ("73", _("73 - Savoie")),
        ("74", _("74 - Haute-Savoie")),
        ("75", _("75 - Paris")),
        ("76", _("76 - Seine-Maritime")),
        ("77", _("77 - Seine-et-Marne")),
        ("78", _("78 - Yvelines")),
        ("79", _("79 - Deux-Sèvres")),
        ("80", _("80 - Somme")),
        ("81", _("81 - Tarn")),
        ("82", _("82 - Tarn-et-Garonne")),
        ("83", _("83 - Var")),
        ("84", _("84 - Vaucluse")),
        ("85", _("85 - Vendée")),
        ("86", _("86 - Vienne")),
        ("87", _("87 - Haute-Vienne")),
        ("88", _("88 - Vosges")),
        ("89", _("89 - Yonne")),
        ("90", _("90 - Territoire de Belfort")),
        ("91", _("91 - Essonne")),
        ("92", _("92 - Hauts-de-Seine")),
        ("93", _("93 - Seine-Saint-Denis")),
        ("94", _("94 - Val-de-Marne")),
        ("95", _("95 - Val-d'Oise")),
        ("971", _("971 - Guadeloupe")),
        ("972", _("972 - Martinique")),
        ("973", _("973 - Guyane")),
        ("974", _("974 - La Réunion")),
        ("976", _("976 - Mayotte"))
    )
    departement = models.CharField(max_length=100, choices=DEPARTEMENT_CHOICES, verbose_name=_("Département"))

    # Critère 2 - Choix du diplôme avec des tuples (valeur, libellé)
    DIPLOME_CHOICES = (
        ("Diplômé d'état", _("Diplômé d'état")),  # Diplômé d'État
        ("Indépendant", _("Indépendant")),  # Diplômé indépendant
    )
    diplome = models.CharField(max_length=20, choices=DIPLOME_CHOICES, verbose_name=_("Diplôme"))
    # Champ pour stocker le document de diplôme
    document_diplome = models.FileField(upload_to='PsyMeetDiplome/', blank=True, null=True, verbose_name=_("Document du diplôme"))

    # Critère 3 - Affichage de la spécialité du psychologue
    SPECIALITE_CHOICES = (
        ("Psychologie clinique", _("Psychologie clinique")),
        ("Psychologie du travail", _("Psychologie du travail")),
        ("Psychologie sociale", _("Psychologie sociale")),
    )
    specialite = models.CharField(max_length=100, choices=SPECIALITE_CHOICES, verbose_name=_("Spécialité"))

    photo = models.FileField(upload_to='PsyMeetPhoto/', blank=True, null=True, verbose_name=_("Photo"))
    nom = models.CharField(max_length=100, verbose_name=_("Nom"))
    prenom = models.CharField(max_length=100, verbose_name=_("Prénom"))
    adresse = models.CharField(max_length=255, verbose_name=_("Adresse"))
    code_postal = models.CharField(max_length=5, verbose_name=_("Code postal"))
    ville = models.CharField(max_length=100, verbose_name=_("Ville"))

    # Champ pour le genre du psychologue avec des choix prédéfinis
    GENRE_CHOICES = (
        ("Homme", _("Homme")),   # Genre masculin
        ("Femme", _("Femme")),   # Genre féminin
    )
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, verbose_name=_("Genre"))

    site_web = models.URLField(blank=True, verbose_name=_("Site web"))
    telephone = models.CharField(max_length=20, verbose_name=_("Téléphone"))
    instagram = models.URLField(blank=True, verbose_name=_("Instagram"))
    facebook = models.URLField(blank=True, verbose_name=_("Facebook"))
    linkedin = models.URLField(blank=True, verbose_name=_("LinkedIn"))
    profil_verifie = models.BooleanField(default=False, verbose_name=_("Profil vérifié"))

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.specialite} - {self.ville}"

    class Meta:
        verbose_name = _("Thérapeute professionnel")
        verbose_name_plural = _("Thérapeutes professionnels")
