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
from django.conf.urls.i18n import i18n_patterns

#urlpatterns = [
#    path('i18n/', include('django.conf.urls.i18n')),  # Pour gérer le changement de langue
#] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    # Administrateur :
    path('lightmeet-admin/', admin.site.urls),

    # Page principale francais - anglais - espagnol / CTA Comparer
    path('', Home.as_view(), name="Home"),
    #path('en/', Home.as_view(), name="Home"),
    #path('sp/',Home.as_view(),name="Home"),

    # Accounts
    #path('connexion', inscription, name="Connexion"),
    #path('connexion/social_network', SocialNetwork, name="Connexion par réseau social"),
    #path('login', login_view, name="login"),
    #path('logout', logout_view, name="logout"),
    #path('connexion/new_account', nouvel_utilisateur, name="nouvel_utilisateur"),
    #path('connexion/forget_password', forget_password, name="forget_password"),
    #path('connexion/delete_account', delete_account, name="Delete Account"),

    # Support
    path('support', SupportContact, name="Support"),
    path('support/Thanks', SupportContact, name="Support-merci"),

    # Legal
    path('legal/mentions_legales/', LegalControlML.as_view(), name="legal_mentions_legales"),
    path('legal/conditions_generales_utilisation', LegalControlCGU.as_view(), name="legal_CGU"),
    path('legal/politique_de_confidentialite/', LegalControlPDC.as_view(), name="legal_PDC"),
    path('legal/politique_de_cookies/', LegalControlPC.as_view(), name="legal_PC"),
    path('legal/mentions_legales/create/', LegalCreate.as_view(), name="legal_create"),
    path('legal/mentions_legales/<str:slug>/', LegalDetail.as_view(), name="legal_detail"),
    path('legal/mentions_legales/edit/<str:slug>/', LegalUpdate.as_view(), name="legal_edit"),
    path('legal/mentions_legales/delete/<str:slug>/', LegalDelete.as_view(), name="legal_delete"),

    # Partner_meet
    path('valid/', enregistrer_visiteur, name="consentement_visiteur"),
    path('rencontres/', PartnerMeetHome.as_view(), name="recherche_home"),
    path('recherche/create/', PartnerMeetCreate.as_view(), name="recherche_create"),
    path('recherche/<int:pk>/', PartnerMeetDetail.as_view(), name="recherche_detail"),
    path('recherche/edit/<int:pk>/', PartnerMeetUpdate.as_view(), name="recherche_edit"),
    path('recherche/delete/<int:pk>/', PartnerMeetDelete.as_view(), name="recherche_delete"),
    path('recherche/site_de_rencontres/', PartnerMeetBestSite.as_view(), name="recherche_meilleur_site"),  # nouveau

    # Psy
    path('therapeutes/', PsyMeetHome.as_view(), name="recherche_therapeutes"),
    path('psy/create', PsyCreate.as_view(), name="psy_create"),
    path('psy/<str:slug>', PsyDetail.as_view(), name="psy_detail"),
    path('psy/edit/<str:slug>', PsyUpdate.as_view(), name="psy_edit"),
    path('psy/delete/<str:slug>', PsyDelete.as_view(), name="psy_delete"),
    path('recherche/sites_des_thérapeutes/', PsyMeetBestSite.as_view(), name="recherche_meilleur_therapeutes"),  # nouveau

    # Blog
    path('blog/main_article',BlogPost1.as_view(), name="blog_home_1"),
    path('blog/second_article',BlogPost2.as_view(), name="blog_home_2"),
    path('blog/menu',BlogPostHome.as_view(), name="blog_home"),
    path('blog/create', BlogPostCreate.as_view(), name="blog_create"),
    path('blog/<str:slug>', BlogPostDetail.as_view(), name="blog_detail"),
    path('blog/edit/<str:slug>', BlogPostUpdate.as_view(), name="blog_edit"),
    path('blog/delete/<str:slug>', BlogPostDelete.as_view(), name="blog_delete"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     # Cette URL permet aux utilisateurs de changer la langue via un formulaire
#     path('i18n/', include('django.conf.urls.i18n')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # Ajoutez les URL multilingues avec i18n_patterns
# urlpatterns += i18n_patterns(
#     # Administrateur :
#     path('lightmeet-admin/', admin.site.urls),

#     # Page principale francais - anglais / CTA Comparer
#     path('', Home.as_view(), name="Home"),

#     # Support
#     path('support/', SupportContact, name="Support"),
#     path('support/Thanks/', SupportContact, name="Support-merci"),

#     # Legal
#     path('legal/mentions_legales/', LegalControlML.as_view(), name="legal_mentions_legales"),
#     path('legal/conditions_generales_utilisation/', LegalControlCGU.as_view(), name="legal_CGU"),
#     path('legal/politique_de_confidentialite/', LegalControlPDC.as_view(), name="legal_PDC"),
#     path('legal/politique_de_cookies/', LegalControlPC.as_view(), name="legal_PC"),
#     path('legal/mentions_legales/create/', LegalCreate.as_view(), name="legal_create"),
#     path('legal/mentions_legales/<str:slug>/', LegalDetail.as_view(), name="legal_detail"),
#     path('legal/mentions_legales/edit/<str:slug>/', LegalUpdate.as_view(), name="legal_edit"),
#     path('legal/mentions_legales/delete/<str:slug>/', LegalDelete.as_view(), name="legal_delete"),

#     # Partner_meet
#     path('valid/', enregistrer_visiteur, name="consentement_visiteur"),
#     path('rencontres/', PartnerMeetHome.as_view(), name="recherche_home"),
#     path('recherche/create/', PartnerMeetCreate.as_view(), name="recherche_create"),
#     path('recherche/<int:pk>/', PartnerMeetDetail.as_view(), name="recherche_detail"),
#     path('recherche/edit/<int:pk>/', PartnerMeetUpdate.as_view(), name="recherche_edit"),
#     path('recherche/delete/<int:pk>/', PartnerMeetDelete.as_view(), name="recherche_delete"),
#     path('recherche/site_de_rencontres/', PartnerMeetBestSite.as_view(), name="recherche_meilleur_site"),

#     # Psy
#     path('therapeutes/', PsyMeetHome.as_view(), name="recherche_therapeutes"),
#     path('psy/create/', PsyCreate.as_view(), name="psy_create"),
#     path('psy/<str:slug>/', PsyDetail.as_view(), name="psy_detail"),
#     path('psy/edit/<str:slug>/', PsyUpdate.as_view(), name="psy_edit"),
#     path('psy/delete/<str:slug>/', PsyDelete.as_view(), name="psy_delete"),
#     path('recherche/sites_des_thérapeutes/', PsyMeetBestSite.as_view(), name="recherche_meilleur_therapeutes"),

#     # Blog
#     path('blog/main_article/', BlogPost1.as_view(), name="blog_home_1"),
#     path('blog/second_article/', BlogPost2.as_view(), name="blog_home_2"),
#     path('blog/menu/', BlogPostHome.as_view(), name="blog_home"),
#     path('blog/create/', BlogPostCreate.as_view(), name="blog_create"),
#     path('blog/<str:slug>/', BlogPostDetail.as_view(), name="blog_detail"),
#     path('blog/edit/<str:slug>/', BlogPostUpdate.as_view(), name="blog_edit"),
#     path('blog/delete/<str:slug>/', BlogPostDelete.as_view(), name="blog_delete"),
# )




