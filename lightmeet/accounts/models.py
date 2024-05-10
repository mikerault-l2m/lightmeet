from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils import timezone
import requests
from django.urls import reverse

class CustomListenerManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Veuillez entrer une adresse email.')
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user

class Lightener(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    birth = models.DateField(null=True)
    prenom = models.CharField(max_length=25, default='')
    consentement = models.BooleanField(default=False)
    weekly_likes = models.PositiveIntegerField(default=0)
    weekly_favorites = models.PositiveIntegerField(default=0)
    last_weekly_reset = models.DateField(default=timezone.now)
    ip_adress = models.GenericIPAddressField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    engagement = models.PositiveIntegerField(default=0)
    favorite_app = models.PositiveIntegerField(default=0)
    clic_comparer = models.PositiveIntegerField(default=0)
    clic_rencontres = models.PositiveIntegerField(default=0)
    clic_therapeutes = models.PositiveIntegerField(default=0)

    def update_ip_and_location(self):
        try:
            # Utilisation du service 'https://api.ipify.org' pour récupérer l'adresse IP publique
            ip_response = requests.get('https://api.ipify.org')
            if ip_response.status_code == 200:
                ip = ip_response.text
                self.ip_address = ip

                # Utilisation du service GeoIP pour obtenir des informations de localisation
                location_response = requests.get(f'http://ip-api.com/json/{ip}')
                if location_response.status_code == 200:
                    location_data = location_response.json()
                    self.location = f"{location_data['city']}, {location_data['regionName']}, {location_data['country']}"
                else:
                    self.location = "Informations de localisation non disponibles"
            else:
                self.ip_address = "Adresse IP non disponible"
                self.location = "Informations de localisation non disponibles"
        except requests.RequestException:
            self.ip_address = "Adresse IP non disponible"
            self.location = "Informations de localisation non disponibles"

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

    USERNAME_FIELD = 'email'
    objects = CustomListenerManager()

    class Meta:
        verbose_name = "Notre compte utilisateur"
        verbose_name_plural = "Nos comptes utilisateurs"

    def __str__(self):
        return self.email if self.email else str(self.id)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
        return