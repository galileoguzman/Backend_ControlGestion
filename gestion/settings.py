"""
Django settings for gestion project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1lo#roz7j^e^06^7e@bm@l1puc!&!hb8cqjrfgk9tw#bs_5v@d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'files',
    'accounts',
    'widget_tweaks',
    
    

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

ROOT_URLCONF = 'gestion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gestion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if not DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'PRODUCTION_INFO_DB',
            'USER': 'PRODUCTION_INFO_DB',
            'PASSWORD': 'PRODUCTION_INFO_DB',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'gestiondb',
            'USER': 'user_gestion_db',
            'PASSWORD' : 'pwd_gestion_db',
            'HOST': 'localhost',
            'PORT': 5432,
        }
    }



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
if not DEBUG:
    # ----------------------------------------------------------------------------
    # AMAZON S3
    # ----------------------------------------------------------------------------

    # CONFIG PERMISSIONS TO S3 BUCKET
    AWS_STORAGE_BUCKET_NAME = 'gestion'
    AWS_ACCESS_KEY_ID = 'YOUR_ACCESS_KEY'
    AWS_SECRET_ACCESS_KEY = 'YOUR_SECRET_ACCESS_KEY'
    AWS_S3_CUSTOM_DOMAIN = "s3-us-west-2.amazonaws.com/%s" % AWS_STORAGE_BUCKET_NAME
    # CONFIG WAY STORAGE TO STATIC AND MEDIA
    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'aws.custom_storages.StaticStorage'
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'aws.custom_storages.MediaStorage'

    # ----------------------------------------------------------------------------
else:
    # ----------------------------------------------------------------------------
    # DEBUG STATIC AND MEDIA FILES
    # ----------------------------------------------------------------------------
    
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/').replace('\\','/')
    MEDIA_URL = '/media/'
    
    STATIC_URL = '/static/'
    STATIC_ROOT = 'staticfiles'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
LOGOUT_REDIRECT_URL = 'index'
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'login'