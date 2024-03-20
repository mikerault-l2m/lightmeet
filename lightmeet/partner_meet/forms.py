from django import forms
from partner_meet.models import *

class PartnerMeetForm(forms.ModelForm):
    class Meta:
        model = PartnerMeet
        fields = '__all__'

