# core\settings.py # DDK

# Use the .env file. See https://django-environ.readthedocs.io/en/latest/quickstart.htmlhttps://pypi.org/project/django-environ/  for all the settings.

import environ

import os # Deze is nodig voor static files te gebruiken die gebruik maakt van 'os'.

# Initialize environment variables
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env()

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# See https://pypi.org/project/django-environ/
# Set the project base directory
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default="unsafe-secret-key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # DDK
    'osbposts',
    'osb_cases',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'static/templates', # deze nodig om ook bij de base.html te komen. # Deze `BASE_DIR` moet dus helemaal bovenaan in `DIRS`, anders gaat het ook niet goed :(
            'templates', # DDK
            'osbposts/templates/osbposts', # DDK deze is ook nodig, wordt niet automatich gevonden gezocht.
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #'django.template.context_processors.media', # Door Dion toegevoegd, echter niet in de tut.
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

""" Dit is de default.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""

DATABASES = { # get the default from the URL above
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'), # Dit is de naam van de database, waarmee we connecten (aangemaakt via `CREATE DATABASE myusername;`)
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/' # Deze is default. Wellicht mooi voor Bootstrap (met in die directory een directroy genaamd 'css')

# Deze is van osbcases. De BASE_DIR kan dus gewoon de BASE_DIR van de app zijn... # vanuit hier kan je met `python3 manage.py collectstatic` alle static folders afgaan.
# Deze is dus de directory die heet 'static' en die in de 'BASE_DIR' zit. De BASE_DIR is de project folder. Met het command collectstatic gaat ie alle 'static' folders af in de app directories.
STATIC_ROOT = os.path.join(BASE_DIR, 'static') 

MEDIA_URL = '' # Dit wordt voro de upload gezet. komt voor de uploads... this will be in the 'media' dir in the root directory. Dit kan soms '/media/' zijn, wat de default is..
# MEDIA_ROOT = os.path.join(BASE_DIR, 'user_uploads') # where do users upload their files, this is defined in the database model, as you upload files from there. 
MEDIA_ROOT = BASE_DIR # This is the files where users upload their files.

# Onderstaande is niet nodig
# STATICFILES_DIRS = [ # Deze variabele is zelf aangemaakt. Deze is gemaakt voor 'obspsots'
#     BASE_DIR / 'static', # Dit is de 'static' directory in het de hoofd directory.
# ]



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
