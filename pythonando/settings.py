"""
Django settings for pythonando project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-op=bfw&m%^w_xe-ymseho0d@!b9sy_2_c7!5m(x0thdzajdj0d'

# SECURITY WARNING: don't run with debug turned on in production! (desenvolvimento ou produção)
DEBUG = True

ALLOWED_HOSTS = ["*"] #qualquer host pode acessar


# Application definition
# apps que o django reconhce e utiliza
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cursos'
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

ROOT_URLCONF = 'pythonando.urls'

# onde estão os templates html
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # caminho dos templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pythonando.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# banco de dados
DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'cursosdb_6hf9',
        'USER': 'admin',
        'PASSWORD': 'oqCZtnX7YFqC4hThnxjVDgA0dSzptj8D',
        'HOST': 'dpg-cvpicfq4d50c73bprorg-a',
        'PORT': '5432',

    }

   #  'default': {
   #      'ENGINE': 'django.db.backends.sqlite3',
   #      'NAME': BASE_DIR / 'db.sqlite3',
   #  }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators
# arquivos dde configuração de autenticação
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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
# arquivos estaticos
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Diretório onde os arquivos estáticos ficam durante o desenvolvimento
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Diretório onde os arquivos serão coletados em produção



# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
