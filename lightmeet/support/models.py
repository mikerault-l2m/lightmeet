from django.db import models
from django.utils.translation import gettext_lazy as _

class SupportTicket(models.Model):

    sender_email = models.EmailField(verbose_name=_("Adresse e-mail de l'expéditeur"))

    SUJET = (
        ("Informations", _("Je souhaite en savoir plus")),
        ("Partenariat", _("Je cherche à réaliser un partenariat")),
        ("Technique", _("Soucis technique sur la plateforme")),
    )
    subject = models.CharField(choices=SUJET, max_length=25, default='', verbose_name=_("Sujet"))
    message = models.TextField(verbose_name=_("Message"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de création"))

    def __str__(self):
        return f"{self.subject} - {self.sender_email}"

    class Meta:
        verbose_name = _("Contact avec le client")
        verbose_name_plural = _("Contacts avec les clients")
