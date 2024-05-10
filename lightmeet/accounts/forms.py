from django import forms
from accounts.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate

# Ce modèle récupère à chaque visite les informations de la part de l'utilisateur.
class LightenerForm(forms.ModelForm):
    class Meta:
        model = Lightener
        fields = ['ip_adress', 'location', 'engagement', 'clic_comparer', 'clic_rencontres', 'clic_therapeutes']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control1", "placeholder": "Adresse email *"})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control1", "placeholder": "Mot de passe *"})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['password'].label = ''

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Identifiants de connexion invalides')
        return cleaned_data

class LightenerCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={"class": "form-control1", "placeholder": "Adresse email *"}))
    birth = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control4", "placeholder": "JJ/MM/AAAA *"}))
    prenom = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class": "form-control5", "placeholder": "Prénom *"}))
    consentement = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={"class": "form-control9"}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control10", "placeholder": "Nouveau mot de passe *"}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control11", "placeholder": "Confirmation du mot de passe *"}))

    class Meta:
        model = Lightener
        fields = ('email', 'birth', 'prenom', 'consentement', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = ''
        self.fields['birth'].label = ''
        self.fields['prenom'].label = ''
        self.fields['consentement'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''

class ForgetForm(UserCreationForm):
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={"class": "form-control1", "placeholder": "Adresse email *"}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control10", "placeholder": "Nouveau mot de passe *"}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"class": "form-control11", "placeholder": "Confirmation du mot de passe *"}))

    class Meta:
        model = Lightener
        fields = ('email','password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
