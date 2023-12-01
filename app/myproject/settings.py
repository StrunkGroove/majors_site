import os

from pathlib import Path

SECRET_KEY = os.getenv('SECRET_KEY')

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.getenv('DEBUG').upper() == 'TRUE'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

CSRF_TRUSTED_ORIGINS = [f"https://{os.getenv('ALLOWED_HOSTS')}"]
CSRF_ALLOWED_ORIGINS = [f"https://{os.getenv('ALLOWED_HOSTS')}"]
CORS_ORIGINS_WHITELIST = [f"https://{os.getenv('ALLOWED_HOSTS')}"]

EXTENSIONS_APP = [
    'main',
    'price',
    'p2plinks',
    'accounts',
    'user_profile',
    'blog',
    'payment',
    'register',
    'links_without_cards',

    'rest_framework',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + EXTENSIONS_APP

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'myproject.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': os.getenv('POSTGRES_PORT'),
    },
    'links_without_cards': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('WITHOUT_PG_NAME'),
        'USER': os.getenv('WITHOUT_PG_USER'),
        'PASSWORD': os.getenv('WITHOUT_PG_PASSWORD'),
        'HOST': os.getenv('WITHOUT_PG_HOST'),
        'PORT': os.getenv('WITHOUT_PG_PORT'),
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://redis:{os.getenv('DEFAULT_REDIS_PORT')}/{os.getenv('DEFAULT_REDIS_NUMBER')}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "p2p_server": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://:{os.getenv('P2P_REDIS_PASSWORD')}@{os.getenv('P2P_REDIS_HOST')}:{os.getenv('P2P_REDIS_PORT')}/{os.getenv('P2P_REDIS_NUMBER')}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}

### Password validation ###

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

### Internationalization ###

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

### USER MODEL ###

AUTH_USER_MODEL = 'accounts.User'

### STATIC FILE configuration ###

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

### LOGGING configuration ###

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'logfile.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}

### REST FRAMEWORK configuration ###

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '60/minute',
        'user': '60/minute',
    }
}

### REDIS configuration ###

CELERY_BROKER_URL = f"redis://redis:{os.getenv('DEFAULT_REDIS_PORT')}/{os.getenv('DEFAULT_REDIS_NUMBER')}"
CELERY_RESULT_BACKEND = f"redis://redis:{os.getenv('DEFAULT_REDIS_PORT')}/{os.getenv('DEFAULT_REDIS_NUMBER')}"
CELERY_TIMEZONE = 'UTC'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASKSERILIZER =  'json'

### Email ###

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS').upper() == 'TRUE'
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


# Settings for self
# if DEBUG is False: 
#     HOST_P2P = os.getenv('HOST_P2P_PROD')
#     HOST_SPOT = os.getenv('HOST_SPOT_PROD')

# elif DEBUG is True:
#     HOST_P2P = os.getenv('HOST_P2P_TEST')
#     HOST_SPOT = os.getenv('HOST_SPOT_TEST')