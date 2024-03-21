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

    path('',Home.as_view(),name = "Home"),

    # Accounts :

    path('connexion', inscription, name="Connexion"),
    path('connexion/social_network',SocialNetwork, name="Connexion par réseau social"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('connexion/new_account',nouvel_utilisateur,name="nouvel_utilisateur"),
    path('connexion/forget_password',forget_password, name="forget_password"),
    path('connexion/delete_account',delete_account,name="Delete Account"),

    # Legal:

    path('mentions_légales', legal_Control_2.as_view(), name="Mentions légales"),
    path('mentions_légales/CGU', legal_Control_CGU.as_view(), name="CGU"),
    path('mentions_légales/PDC', legal_Control_PDC.as_view(), name="PDC"),
    path('mentions_légales/PC', legal_Control_PC.as_view(), name="PC"),
    #path('legal/consentement',legal_consentement.as_view(),name="Consentement"),

    # Partner_meet:

    # Cette API propose de filtrer les applications de rencontre afin de proposer le meilleur aux célibataires.
    path('rencontre/',rencontrer.as_view(),name = "Rencontres"),

    # Thérapeutes :
    path('psy/',psy_control_2.as_view(),name = "Psychologue"),

    # Support :
    path('contact/',SupportModel.as_view(),name="Contact"),

    #Blog
    path('blog/',BlogHome.as_view(),name="blog_home"),
    path('blog/create',login_required(BlogPostCreate.as_view()),name="blog_create"),
    path('blog/<str:slug>',BlogPostDetail.as_view(),name="blog_detail"),
    path('blog/edit/<str:slug>',login_required(BlogPostUpdate.as_view()),name="blog_edit"),
    path('blog/delete/<str:slug>',login_required(BlogPostDelete.as_view()),name="blog_delete")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)