import os
import environ
from pathlib import Path
#from django.utils.translation import gettext as _

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()

environ.Env.read_env(env_file=str(BASE_DIR / "lightmeet" / ".env"))

SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

LOCAL_APPS = [
    'accounts',
    'legal',
    'posts',
    'support',
    'presse',
    'psy',
    'partner_meet',
]
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # AJOUT POUR PACKAGE ALLAUTH
    'django.contrib.sites',
]
THIRD_PARTY_APPS = [
    # AJOUT POUR PACKAGE ALLAUTH
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Les apps pour se conencter avec google et facebook ci-dessous
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Déplacer après AuthenticationMiddleware
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'responsive.middleware.DeviceInfoMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = (
    # Other context processors included here
    'responsive.context_processors.device_info',
)

ROOT_URLCONF = 'lightmeet.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'lightmeet/templates'),
                    os.path.join(BASE_DIR, 'posts/templates'),
                    os.path.join(BASE_DIR, 'legal/templates'),
                    os.path.join(BASE_DIR, 'partner_meet/templates'),
                    os.path.join(BASE_DIR, 'psy/templates'),
                    os.path.join(BASE_DIR, 'presse/templates'),
                    os.path.join(BASE_DIR, 'accounts/templates'),
                    os.path.join(BASE_DIR, 'support/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'responsive.context_processors.device_info',  # Ajouter ce context processor
            ],
        },
    },
]

WSGI_APPLICATION = 'lightmeet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
     'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
     }
 }


#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'lightmeet',
#        'USER': 'mike',
#       'PASSWORD': 'votre_mot_de_passe_postgresql',
#       'HOST': 'localhost',  # Ou l'adresse IP de votre serveur PostgreSQL
#        'PORT': '5432',            # Laissez vide pour utiliser le port par défaut (5432)
#    }
#}

#LANGUAGES = [
#    ('en',_('English')),
#    ('fr',_('French')),
#    ('sp',_('Spanish'))]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    # AJOUT POUR PACKAGE ALLAUTH
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'fr-fr'


TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

LOGIN_REDIRECT_URL = '/accounts/'

LOGOUT_URL = 'logout'
#
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
AUTH_USER_MODEL = 'accounts.Lightener'

SITE_ID = 1

# settings.py
USER_MODEL_USERNAME_FIELD = 'email'
ACCOUNT_AUTHENTICATION_METHOD = 'email'

#AJOUT ci-dessous pour corriger bug, sinon doit changer
# ACCOUNT_AUTHENTICATION_METHOD en autre chose que 'email'
# cf https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED=True

ACCOUNT_EMAIL_VERIFICATION = "none"