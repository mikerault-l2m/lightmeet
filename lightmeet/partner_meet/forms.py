from django import forms
from partner_meet.models import *

class PartnerMeetForm(forms.ModelForm):
    class Meta:
        model = PartnerMeet
        fields = '__all__'

class ComparateurForm(forms.ModelForm):
    class Meta:
        model = Comparateur
        fields = '__all__'
        # widgets = {
        #     'genre': forms.Select(choices=(('femmes', 'Femmes'), ('hommes', 'Hommes'), ('tous', 'Tous'))),
        #     'relation': forms.Select(choices=(('durables', 'Durables'), ('Relation d''un soir', 'Relation d'' un soir'), ('toutes', 'Toutes'))),
        #     'age': forms.Select(choices=(('18-25', '18-25 ans'), ('25-35', '25-35 ans'), ('35-45', '35-45 ans'), ('45-55', '45-55 ans'), ('plus', 'Plus de 55 ans')))
        # }

