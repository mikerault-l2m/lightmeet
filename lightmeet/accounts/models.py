from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import requests

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name=_("Adresse IP"))
    location = models.CharField(max_length=100, blank=True, verbose_name=_("Localisation"))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_("Horodatage"))

    class Meta:
        verbose_name = _("Visiteur de Lightmeet")
        verbose_name_plural = _("Visiteurs de Lightmeet")

class CustomListenerManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError(_("L'adresse e-mail est obligatoire."))
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Lightener(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, verbose_name=_("E-mail"))
    is_active = models.BooleanField(default=True, verbose_name=_("Actif"))
    is_staff = models.BooleanField(default=False, verbose_name=_("Membre du personnel"))
    is_admin = models.BooleanField(default=False, verbose_name=_("Administrateur"))
    birth = models.DateField(null=True, blank=True, verbose_name=_("Date de naissance"))
    prenom = models.CharField(max_length=25, blank=True, verbose_name=_("Prénom"))
    consentement = models.BooleanField(default=False, verbose_name=_("Consentement"))
    weekly_likes = models.PositiveIntegerField(default=0, verbose_name=_("J'aime hebdomadaires"))
    weekly_favorites = models.PositiveIntegerField(default=0, verbose_name=_("Favoris hebdomadaires"))
    last_weekly_reset = models.DateField(default=timezone.now, verbose_name=_("Dernière réinitialisation hebdomadaire"))
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name=_("Adresse IP"))
    location = models.CharField(max_length=100, blank=True, verbose_name=_("Localisation"))
    engagement = models.PositiveIntegerField(default=0, verbose_name=_("Engagement"))
    favorite_app = models.PositiveIntegerField(default=0, verbose_name=_("Application préférée"))
    clic_comparer = models.PositiveIntegerField(default=0, verbose_name=_("Clics Comparer"))
    clic_rencontres = models.PositiveIntegerField(default=0, verbose_name=_("Clics Rencontres"))
    clic_therapeutes = models.PositiveIntegerField(default=0, verbose_name=_("Clics Thérapeutes"))

    USERNAME_FIELD = 'email'
    objects = CustomListenerManager()

    class Meta:
        verbose_name = _("Compte utilisateur")
        verbose_name_plural = _("Comptes utilisateurs")

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def update_ip_and_location(self):
        try:
            ip_response = requests.get('https://api.ipify.org')
            if ip_response.status_code == 200:
                ip = ip_response.text
                self.ip_address = ip

                location_response = requests.get(f'http://ip-api.com/json/{ip}')
                if location_response.status_code == 200:
                    location_data = location_response.json()
                    self.location = f"{location_data.get('city', _('Ville inconnue'))}, {location_data.get('regionName', _('Région inconnue'))}, {location_data.get('country', _('Pays inconnu'))}"
                else:
                    self.location = _("Informations de localisation non disponibles")
            else:
                self.ip_address = _("Adresse IP non disponible")
                self.location = _("Informations de localisation non disponibles")
        except requests.RequestException:
            self.ip_address = _("Adresse IP non disponible")
            self.location = _("Informations de localisation non disponibles")

    def increment_weekly_likes(self):
        self.weekly_likes += 1
        self.save()

    def increment_weekly_favorites(self):
        self.weekly_favorites += 1
        self.save()

    def increment_clic_comparer(self):
        self.clic_comparer += 1
        self.save()

    def increment_clic_rencontres(self):
        self.clic_rencontres += 1
        self.save()

    def increment_clic_therapeutes(self):
        self.clic_therapeutes += 1
        self.save()
