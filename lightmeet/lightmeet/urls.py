from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from partner_meet.views import *
from accounts.views import *
from legal.views import *
from psy.views import *
from support.views import *
from posts.views import *

urlpatterns = [
            # Administrateur :
        path('lightmeet-admin/', admin.site.urls),

        # Page principale / CTA Comparer
        path('',Home.as_view(),name = "Home"),

            # Accounts

        # Connexion de l'utilisateur
        path('connexion', inscription, name="Connexion"),

        # Connexion par le biais des réseaux sociaux
        path('connexion/social_network',SocialNetwork, name="Connexion par réseau social"),

        # Principe de connexion
        path('login', login_view, name="login"),

        # Principe de déconnexion
        path('logout', logout_view, name="logout"),

        # Création d'un compte
        path('connexion/new_account',nouvel_utilisateur,name="nouvel_utilisateur"),

        # Mot de passe oublié
        path('connexion/forget_password',forget_password, name="forget_password"),

        # Supprimer son compte
        path('connexion/delete_account',delete_account,name="Delete Account"),

            # Legal

        # Affichage des mentions légales de Lightmeet
        path('mentions_légales', legal_Control_2.as_view(), name="Mentions légales"),

        # Affichage des CGU
        path('mentions_légales/CGU', legal_Control_CGU.as_view(), name="CGU"),

        # Affichage des politiques de confidentialité
        path('mentions_légales/PDC', legal_Control_PDC.as_view(), name="PDC"),

        # Affichage des politiques des cookies
        path('mentions_légales/PC', legal_Control_PC.as_view(), name="PC"),

        # Obtention du consentement de l'utilisateur
        #path('legal/consentement',legal_consentement.as_view(),name="Consentement"),

            # Partner_meet:

        # Outil de recherche de sites de rencontre
        #path('recherche/',rencontrer.as_view(),name = "Rencontres"),

        path('recherche/',partner_meet_formulaire.as_view(),name = "partner_meet_formulaire"),

        # Outil de comparaison de marques de rencontre
        # path('rencontre/comparaison',meet_compare.as_view(),name = "Comparaison Rencontres"),

        # Thérapeutes :

        # Outil de recherche de thérapeutes géolocalisés
        #path('psy/',psy_control_2.as_view(),name = "Psychologue"),

        # Outil de comparaison entre thérapeutes géolocalisés
        #path('psy/thérapeutes',psy_control_2.as_view(),name = "Psychologue"),

        # Support :

        # Formulaire pour contacter l'entreprise Lightmeet
        #path('contact/',SupportModel.as_view(),name="Contact"),

        # Blog

        # Page principale du blog -
        path('blog/',BlogHome.as_view(),name="blog_home"),

        # Création d'articles sur le Blog
        path('blog/create',login_required(BlogPostCreate.as_view()),name="blog_create"),

        # Ciblage d'un article suivant le nom de l'article
        path('blog/<str:slug>',BlogPostDetail.as_view(),name="blog_detail"),

        # Édition d'un article ciblé suivant le nom de l'article
        path('blog/edit/<str:slug>',login_required(BlogPostUpdate.as_view()),name="blog_edit"),

        # Suppression d'un article
        path('blog/delete/<str:slug>',login_required(BlogPostDelete.as_view()),name="blog_delete")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)