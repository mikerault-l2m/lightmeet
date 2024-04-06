from django import forms
from partner_meet.models import *

class PartnerMeetForm(forms.ModelForm):
    class Meta:
        model = PartnerMeet
        fields = '__all__'

class ComparateurForm(forms.ModelForm):
    genre = forms.ChoiceField(widget=forms.Select(attrs={'style': 'background-color: yellow; font-size: 1.1em;'}))
    age = forms.ChoiceField(widget=forms.Select(attrs={'style': 'background-color: yellow; font-size: 1.1em;'}))
    relation = forms.ChoiceField(widget=forms.Select(attrs={'style': 'background-color: yellow; font-size: 1.1em;'}))

    class Meta:
        model = Comparateur
        fields = '__all__'

