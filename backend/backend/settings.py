"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from corsheaders.defaults import default_headers


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4u(^+6w9z@4yjzf(r_1e)i76#h9v54!q2*=m0y-&t#2(f)1^e7'
# DEBUG = 0
DEBUG = bool(int(os.environ.get('DEBUG', '0')))

# SECURITY WARNING: don't run with debug turned on in production!


ALLOWED_HOSTS = [
	"hoodiyalko.com.ua",
	"hoodiyalko.avallon.im",
	"localhost",
]

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'app',
	'corsheaders',
	'django.contrib.staticfiles',
	'adminsortable2',
	'sorl.thumbnail',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
	# 'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'])}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

# STATIC_ROOT = os.environ['STATIC_ROOT']

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.environ['MEDIA_ROOT']

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = list(default_headers) + [
	'sentry-trace',
	'Access-Control-Allow-Headers',
	'Access-Control-Allow-Credentials',
]

CORS_ORIGIN_WHITELIST = [
	'http://localhost:8080',
	'https://hoodiyalko.avallon.im',
]

SITE_URL = os.environ['SITE_URL']

NOVAPOSHTA_API_KEY = 'cd0fe6f50623590fa01e0ad0a88aaaad'

EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = "lith2009@mail.ru"
EMAIL_HOST_PASSWORD = "zvada1601"
EMAIL_USE_TLS = True

FROM_EMAIL = 'admin <lith2009@mail.ru>'

ADMIN_EMAILS = [
	"dmitryzvada@gmail.com",
	"hoodiyalko@gmail.com",
]

THUMBNAIL_FORMAT = 'PNG'
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_REDIS_HOST = 'localhost'
THUMBNAIL_REDIS_PORT = 6379

sentry_sdk.init(
	dsn="https://6df622b069b8449fbe56509e5546f5a6@o498785.ingest.sentry.io/5578609",
	integrations=[DjangoIntegration()],
	traces_sample_rate=1.0,

	# If you wish to associate users to errors (assuming you are using
	# django.contrib.auth) you may enable sending PII data.
	send_default_pii=True
)

