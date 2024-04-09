from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
    path('', Home.as_view(), name="Home"),

    # Accounts
    #path('connexion', inscription, name="Connexion"),
    #path('connexion/social_network', SocialNetwork, name="Connexion par réseau social"),
    #path('login', login_view, name="login"),
    #path('logout', logout_view, name="logout"),
    #path('connexion/new_account', nouvel_utilisateur, name="nouvel_utilisateur"),
    #path('connexion/forget_password', forget_password, name="forget_password"),
    #path('connexion/delete_account', delete_account, name="Delete Account"),

    # Legal
    path('mentions_légales/', LegalHome.as_view(), name="legal_home"),
    path('mentions_légales/create/', LegalCreate.as_view(), name="legal_create"),
    path('mentions_légales/<str:slug>/', LegalDetail.as_view(), name="legal_detail"),
    path('mentions_légales/edit/<str:slug>/', LegalUpdate.as_view(), name="legal_edit"),
    path('mentions_légales/delete/<str:slug>/', LegalDelete.as_view(), name="legal_delete"),

    # Partner_meet
    path('recherche/', PartnerMeetHome.as_view(), name="recherche_home"),
    path('recherche/create/', PartnerMeetCreate.as_view(), name="recherche_create"),
    path('recherche/<int:pk>/', PartnerMeetDetail.as_view(), name="recherche_detail"),
    path('recherche/edit/<int:pk>/', PartnerMeetUpdate.as_view(), name="recherche_edit"),
    path('recherche/delete/<int:pk>/', PartnerMeetDelete.as_view(), name="recherche_delete"),

    #Support
    path('support/', SupportModel.as_view(), name="Contact"),

    # Blog
    path('blog/', BlogHome.as_view(), name="blog_home"),
    path('blog/create', BlogPostCreate.as_view(), name="blog_create"),
    path('blog/<str:slug>', BlogPostDetail.as_view(), name="blog_detail"),
    path('blog/edit/<str:slug>', BlogPostUpdate.as_view(), name="blog_edit"),
    path('blog/delete/<str:slug>', BlogPostDelete.as_view(), name="blog_delete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
