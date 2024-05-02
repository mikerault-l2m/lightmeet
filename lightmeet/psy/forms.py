from django import forms
from psy.models import *


class PsyMeetForm(forms.ModelForm):
    class Meta:
        model = PsyMeet
        fields = '__all__'