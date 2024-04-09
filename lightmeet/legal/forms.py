from django import forms
from legal.models import *

class LegalForm(forms.ModelForm):
    class Meta:
        model = Legal
        fields = '__all__'
