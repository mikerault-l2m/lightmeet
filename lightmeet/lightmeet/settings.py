import os
import environ
from pathlib import Path
from django.utils.translation import gettext_lazy, gettext as _

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
    # Les apps pour se conencter avec google et facebook ci-dessous
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
    'allauth.account.middleware.AccountMiddleware',  # Déplacer après AuthenticationMiddleware
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

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
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

LANGUAGE_CODE = 'fr-fr'


TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    #('en-us', 'English'),
    ('fr', 'French'),
    ('de', 'Deutsch'),
    ('es','Spanish'),
    ('nl', 'Nederlands'),
    ('it', 'Italiano'),
]

# Test de traduction par gettext_noop à tester
# LANGUAGE_CODE = "en-us"

#LANGUAGES = [
    # Europe de l'Est :
    # ("az", gettext_noop("Azerbaijani")),
    # ("bg", gettext_noop("Bulgarian")),
    # ("be", gettext_noop("Belarusian")),
    # ("bs", gettext_noop("Bosnian")),
    # ("cs", gettext_noop("Czech")),
    # ("et", gettext_noop("Estonian")),
    # ("hr", gettext_noop("Croatian")),
    # ("hu", gettext_noop("Hungarian")),
    # ("lt", gettext_noop("Lithuanian")),
    # ("lv", gettext_noop("Latvian")),
    # ("mk", gettext_noop("Macedonian")),
    # ("pl", gettext_noop("Polish")),
    # ("ro", gettext_noop("Romanian")),
    # ("ru", gettext_noop("Russian")),
    # ("sk", gettext_noop("Slovak")),
    # ("sl", gettext_noop("Slovenian")),
    # ("sq", gettext_noop("Albanian")),
    # ("sr", gettext_noop("Serbian")),
    # ("sr-latn", gettext_noop("Serbian Latin")),
    # ("uk", gettext_noop("Ukrainian")),

    # Europe du Nord / Ouest :
    # ("da", gettext_noop("Danish")),
    # ("de", gettext_noop("German")),
    # ("en", gettext_noop("English")),
    # ("en-au", gettext_noop("Australian English")),
    # ("en-gb", gettext_noop("British English")),
    # ("fi", gettext_noop("Finnish")),
    # ("fr", gettext_noop("French")),
    # ("fy", gettext_noop("Frisian")),
    # ("ga", gettext_noop("Irish")),
    # ("gd", gettext_noop("Scottish Gaelic")),
    # ("is", gettext_noop("Icelandic")),
    # ("it", gettext_noop("Italian")),
    # ("nl", gettext_noop("Dutch")),
    # ("nb", gettext_noop("Norwegian Bokmål")),
    # ("sv", gettext_noop("Swedish")),
    # ("gl", gettext_noop("Galician")),
    # ("pt", gettext_noop("Portuguese")),

    # Afrique :
    # ("kab", gettext_noop("Kabyle")),
    # ("sw", gettext_noop("Swahili")),
    # ("ig", gettext_noop("Igbo")),
    # ("mg", gettext_noop("Malagasy")),  # Madagascar ajouté

    # Amérique du Nord et du Sud :
    # ("es", gettext_noop("Spanish")),
    # ("es-ar", gettext_noop("Argentinian Spanish")),
    # ("es-co", gettext_noop("Colombian Spanish")),
    # ("es-mx", gettext_noop("Mexican Spanish")),
    # ("es-ni", gettext_noop("Nicaraguan Spanish")),
    # ("es-ve", gettext_noop("Venezuelan Spanish")),
    # ("pt-br", gettext_noop("Brazilian Portuguese")),

    # Asie :
    # ("bn", gettext_noop("Bengali")),
    # ("fa", gettext_noop("Persian")),
    # ("he", gettext_noop("Hebrew")),
    # ("hi", gettext_noop("Hindi")),
    # ("id", gettext_noop("Indonesian")),
    # ("ja", gettext_noop("Japanese")),
    # ("km", gettext_noop("Khmer")),
    # ("ko", gettext_noop("Korean")),
    # ("ml", gettext_noop("Malayalam")),
    # ("my", gettext_noop("Burmese")),
    # ("ne", gettext_noop("Nepali")),
    # ("ta", gettext_noop("Tamil")),
    # ("te", gettext_noop("Telugu")),
    # ("th", gettext_noop("Thai")),
    # ("vi", gettext_noop("Vietnamese")),
    # ("zh-hans", gettext_noop("Simplified Chinese")),
    # ("zh-hant", gettext_noop("Traditional Chinese")),

    # Moyen-Orient et Asie Centrale :
    # ("hy", gettext_noop("Armenian")),
    # ("ka", gettext_noop("Georgian")),
    # ("kk", gettext_noop("Kazakh")),
    # ("ky", gettext_noop("Kyrgyz")),
    # ("tg", gettext_noop("Tajik")),
    # ("tk", gettext_noop("Turkmen")),
    # ("tr", gettext_noop("Turkish")),
#]


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
ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = "none"
