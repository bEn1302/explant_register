from pathlib import Path
from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv
from datetime import timedelta
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG') == 'True'

ALLOWED_HOSTS = ['*', 'https://explantregister-production.up.railway.app', 'https://explantregister-testing.up.railway.app']


# Application definition

INSTALLED_APPS = [
    'multi_captcha_admin',
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'whitenoise.runserver_nostatic',
    'data',
    'users',

    'captcha',
    'import_export',
    'rosetta',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_auto_logout.middleware.auto_logout',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "https://explantregister-production.up.railway.app",
    "https://explantregister-testing.up.railway.app",
    # ... Weitere vertrauenswürdige Ursprungs-URLs
]

CSRF_TRUSTED_ORIGINS = ['https://explantregister-production.up.railway.app','https://explantregister-testing.up.railway.app']

ROOT_URLCONF = 'ExReg.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_auto_logout.context_processors.auto_logout_client',
                'data.context_processors.user_is_expert_or_moderator',
            ],
        },
    },
]

WSGI_APPLICATION = 'ExReg.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'viaduct.proxy.rlwy.net',
        'PORT': '37825',
    }
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

LANGUAGE_CODE = 'de'

LANGUAGES = [
    ('de', _('Deutsch')),
    ('en', _('Englisch')),
]

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

ROSETTA_REQUIRES_AUTH = True

TIME_ZONE = 'UTC'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880

STATICFILES_DIRS = ( 
      os.path.join(BASE_DIR, 'static'),

)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auto Logout Function
AUTO_LOGOUT = {
    'IDLE_TIME': timedelta(minutes=30),
    'SESSION_TIME': timedelta(hours=2),
    'MESSAGE': 'The session has expired. Please login again to continue.',
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
}

# recaptcha
MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}

# Jazzmin (https://django-jazzmin.readthedocs.io/)
JAZZMIN_SETTINGS = {
    "site_title": "ExReg Admin",
    "site_header": "ExReg",
    "site_brand": "ExReg",
    "site_icon": "img/favicon.svg",
    "welcome_sign": "Welcome to ExReg",
    "copyright": "ExReg",
}