from django.db import models

class SupportTicket(models.Model):

    sender_email = models.EmailField()
    SUJET = (
    ("Informations","Je souhaite en savoir plus"),
    ("Partenariat","Je cherche à réaliser un partenariat"),
    ("Technique","Soucis technique sur la plateforme"),
)
    subject = models.CharField(choices=SUJET,max_length=25,default='')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.sender_email}"

    class Meta:
        verbose_name = "Notre contact avec le client"
        verbose_name_plural = "Nos contacts avec les clients"
