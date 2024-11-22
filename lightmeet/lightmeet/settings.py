import os
import environ
from pathlib import Path
from django.utils.translation import gettext_lazy as _

# -*- coding: utf-8 -*-

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
    'locale',
    'support',
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
    'django.contrib.sites',
    'modeltranslation',
]
THIRD_PARTY_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'responsive.middleware.DeviceInfoMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = (
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
                 os.path.join(BASE_DIR, 'accounts/templates'),
                 os.path.join(BASE_DIR, 'support/templates'),
                 os.path.join(BASE_DIR, 'lightmeet/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'responsive.context_processors.device_info',
            ],
        },
    },
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

WSGI_APPLICATION = 'lightmeet.wsgi.application'

DATABASES = {
     'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
     }
 }

# Configurations de langue pour les variantes d'anglais international et autres langues
LANGUAGE_CODE = 'fr-fr'
LANGUAGES = [
    ('en-us', _('English (US)')),
    ('fr', _('French')),
    ('de', _('German')),
    ('da', _('Danish')),
    ('pt', _('Portuguese')),
    ('nl', _('Dutch')),
    ('es', _('Spanish')),
]

# Fuseaux horaires, choisissez un fuseau adapté :
TIME_ZONE = 'America/New_York'  # Option pour le public américain
# TIME_ZONE = 'Europe/London'  # Option pour le public britannique
# TIME_ZONE = 'Australia/Sydney'  # Option pour le public australien
# TIME_ZONE = 'America/Toronto'  # Option pour le public canadien

USE_I18N = True
USE_L10N = True
USE_TZ = True

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
    'allauth.account.auth_backends.AuthenticationBackend',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

LOGIN_REDIRECT_URL = '/accounts/'
LOGOUT_URL = 'logout'

AUTH_USER_MODEL = 'accounts.Lightener'

SITE_ID = 1

USER_MODEL_USERNAME_FIELD = 'email'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
