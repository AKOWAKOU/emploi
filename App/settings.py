

from pathlib import Path
import dj_database_url
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'django-insecure-e=su4&i0eyz*h&w7ynxo@^u36x$ktm=gbj)r)2g7nas2@e!s6p'
DEBUG = os.getenv("DEBUG", "False") == "True"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =True

ALLOWED_HOSTS = ['example-emploi-service.onrender.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Auth',
    'TimeTable',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    
]

ROOT_URLCONF = 'App.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'App.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    },
    # 'default': {  
    #     'ENGINE': 'django.db.backends.mysql',  
    #     'NAME': 'pil_database',  
    #     'USER': 'root',  
    #     'PASSWORD': '',  
    #     'HOST': '127.0.0.1',  
    #     'PORT': '3306',  
    #     'OPTIONS': {  
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
    #     }  
    # }
}

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL", "postgresql://emploi_database_user:tjCizrmXOQlUZvdxWyWcpjFnPiQBy7Dl@dpg-csmdmstds78s73ee5hc0-a.oregon-postgres.render.com/emploi_database")
    )
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Africa/Porto-Novo'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [ BASE_DIR / 'static/' ]

MEDIA_ROOT = BASE_DIR / 'media/'

MEDIA_URL = '/media/'
LOGIN_URL = '/auth/login'

AUTH_USER_MODEL = 'Auth.User'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'TimeTable - IFRI <timetable239@gmail.com>'
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
STATIC_URL = 'static/'

# Where collected static files will be stored
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media/'
MEDIA_URL = '/media'
