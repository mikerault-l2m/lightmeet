from django.shortcuts import render,redirect
from accounts.forms import *
from accounts.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
import time


def inscription(request):
    form = CustomAuthenticationForm()
    return render(request, "accounts/signup.html", context={"form": form})

def SocialNetwork(request):
    return render(request, "accounts/ConnexionFacebook.html")

@login_required
def delete_account(request):
    if request.method == 'POST':
        # Perform actions to delete the user account, such as:
        user = request.user
        user.delete()

        # You may also want to log the user out after deletion
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('home')

    return render(request, 'delete_account.html')  # Create a template for the confirmation page
########### Connexion
def login_view(request):
    # If the user submitted the login form
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Log the user in and redirect to the home page
            login(request, user)
            return redirect('Programme Frileux')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/signup.html', {'form':form})

 # Redirect to the home page or any other desired page after deletion

#### Déconnexion
def logout_view(request):
    logout(request)
    return redirect('page_accueil')

######## Création de compte
def nouvel_utilisateur(request):
    if request.method == "POST":
        form = CustomListenerForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            email = form.cleaned_data.get("password")
            password = new_user.password  # Remplacez cela par un mot de passe sécurisé
            # Génération de la paire de clés et stockage de la clé publique
            # public_key, encrypted_key_filename = generate_and_store_rsa_key_pair(email, password,"/home/mikerault/listen2meet/listen2meet/accounts/keys")
            min_val, max_val = 111111, 999999
            code =  random.randint(min_val, max_val)
            context = {"form": code}
            return render(request, "accounts/Check_Email.html", context)
        else:
            print(form.error_messages)
    else:
        form = CustomListenerForm()
        context = {"form": form, "error_messages": form.errors}
    return render(request, "accounts/New_User.html", context={"form": form})

######## Mot de passe oublié

def forget_password(request):
    if request.method == "POST":
        form = ForgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("page_accueil")
    else:
        form = ForgetForm()
    return render(request, "accounts/Forget_Password.html", context={"form": form})
