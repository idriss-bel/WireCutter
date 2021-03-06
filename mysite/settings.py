"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c4e!j5x(l_wk^i*zalq1f07dz8ddb#pv%$leqfz8pxs)!pqksd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'polls',
    'south',
    'markdown_deux',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
## for SQL-lite3
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
## for MySQL
        'ENGINE': 'django.db.backends.mysql',           # Add 'prostgresql_psycopg2', 'mysql', 'sqlite3', or 'oracle'
        'NAME': 'wirecutter_db',
        'USER': 'root',
        'PASSWORD': 'Get0ut:123',
        'HOST': '',                                     # Empty for localhost through domain sockets or '127.0.0.1' for localhost through
        'PORT': '',                                     # Set to empty string for default.
    }
}



#TEMPLATE_DIRS = ('/Users/richleung/Projects/WireCutter_proj/mysite/templates')
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
    # Put strings here, like "/home/html/django_templates" or "C:/www.django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relatives paths.

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
