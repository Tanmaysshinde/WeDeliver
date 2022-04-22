"""
Django settings for WebProject project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vk5p6s#^t#cjb)q9*)gj6-qb1&c)04j3#@^tlvlp624$fxmf()'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'wedeliver123.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'WeDeliver',
    'widget_tweaks',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
]

STATICFILES_STORAGE =  'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'WebProject.urls'

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

WSGI_APPLICATION = 'WebProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'WeDeliver',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': '9987793650',
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


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR,'static')

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static/')
# ]

MEDIA_URL = '/profilepic/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'profilepic')

SITE_ID = 1

LOGIN_REDIRECT_URL = "/WeDeliver/"

LOGIN_REQUIRED_URL = "/WeDeliver/"  

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
    'face_book' :{
        'SCOPE': [
            'public_profile',
            'email',
        ],
    },
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {
        "": {"handlers": ["console"], "level": "INFO"},
        "django": {"handlers": ["console"], "level": "INFO"},
    },
}

# Activate Django-Heroku settings except logging
django_heroku.settings(locals(), logging=False)

# SESSION_COOKIE_AGE = 14000

# SESSION_EXPIRE_SECONDS = 14000

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_TIMEOUT_REDIRECT = '/WeDeliver/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GOOGLE_API_KEY = 'AIzaSyDzXEs-EuKe3-pBGP5UB-NUNa20LLTnmXs'

RAZORPAY_KEY = 'rzp_test_YeUQJn3xhNMSok'

RAZORPAY_SECRET_KEY = 'YMTDA6EkqhUMEm5txnBuItQs'

VONAGE_API_KEY = '6694db49'

VONAGE__API_SECRET_KEY = '4z967EFntN6W3dqK'

SENDINBLUE_API_KEY = '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'

EMAIL_HOST_USER = 'tanmayshinde79@gmail.com'

EMAIL_HOST = 'WeDeliver'