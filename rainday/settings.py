"""
Django settings for rainday project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import json
import os
from pathlib import Path
from platform import system as sys

from dotenv import load_dotenv, dotenv_values

BASE_DIR = Path(__file__).resolve().parent.parent

try:
    ENV_FILE = json.load(open(os.path.join(BASE_DIR, "keys.json")))
except FileNotFoundError:
    ENV_LOC = BASE_DIR / "rainday/.env"
    ENV_LOAD = load_dotenv(ENV_LOC)
    ENV_FILE = dotenv_values(ENV_LOC)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-**a)w#p&5&yenp4i*o$7%zd@juu*@=4+zcbij5oj%wt052%q)("

# SECURITY WARNING: don't run with debug turned on in production!
if sys().lower().startswith("windows") or sys().lower().startswith("darwin"):
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "rainday.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "rainday.wsgi.application"

AUTH_USER_MODEL = "app.User"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "NAME": "rainday",
        "ENGINE": "django.db.backends.mysql",
        "USER": ENV_FILE.get("DB_USER"),
        "PASSWORD": ENV_FILE.get("DB_PASS"),
        "HOST": ENV_FILE.get("DB_HOST"),
        "PORT": "3306",
        "OPTIONS": {
            "autocommit": True,
            "charset": "utf8mb4",
        },
    }
}
# DATABASES = {
#     "default": {
#         "NAME": "rainday",
#         "ENGINE": "django.db.backends.mysql",
#         "USER": 'root',
#         "PASSWORD": '0315',
#         "HOST": 'localhost',
#         "PORT": "3306",
#         "OPTIONS": {
#             "autocommit": True,
#             "charset": "utf8mb4",
#         },
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


"""
    GMAIL
"""
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True


EMAIL_HOST_PASSWORD = ENV_FILE.get("GMAIL_AUTH")
EMAIL_HOST_USER = ENV_FILE.get("GMAIL_ADDR")

