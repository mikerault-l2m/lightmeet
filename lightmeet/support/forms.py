from django.forms import ModelForm
from django import forms
from support.models import *


# Formulaire basé sur le modèle SupportTicket
class SupportTicketForm(ModelForm):
    required_css_class = "required_field"

    sender_email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": " Adresse e-mail *"
        })
    )

    subject = forms.ChoiceField(
        required=True,
        choices=SupportTicket.SUJET,
        widget=forms.Select(attrs={
            "class": "form-control",
            "placeholder": "Le sujet de ton choix *"
        })
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": " Contenu du message *"
        })
    )

    class Meta:
        model = SupportTicket
        fields = ['sender_email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sender_email'].label = ''
        self.fields['subject'].label = ''
        self.fields['message'].label = ''