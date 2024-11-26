import os
from datetime import timedelta
from pathlib import Path

import dj_database_url
from corsheaders.defaults import default_headers
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

MODE = os.getenv("MODE")

SECRET_KEY = os.getenv(
    "SECRET_KEY", "g0_wu2u9w19u4_ej=x*i%jz1ye=t1s$3ax#met!u!=^1x#x2o0"
)
DEBUG = os.getenv("DEBUG", "False")
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["http://*, https://*"]

API_URL = os.getenv("API_URL", "http://localhost:8000")
BASE_URL = os.getenv("API_URL", "http://localhost:8000")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "corsheaders",
    "safedelete",
    "django_filters",
    "core.company.infra.company_django_app",
    "core.populate.infra.populate_django_app",
    "core.uploader.infra.uploader_django_app",
    "core.user.infra.user_django_app",

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_project.middleware.CompanyMiddleware",
]

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "django_project.wsgi.application"

if MODE == "dev":
    DATABASES = {
        "default": dj_database_url.config(
            default=os.getenv("DATABASE_URL_DEV", "sqlite://f{BASE_DIR}/db.sqlite3")
        )
    }
elif MODE == "staging":
    DATABASES = {
        "default": dj_database_url.config(
            default=os.getenv("DATABASE_URL_STAGING", "sqlite://f{BASE_DIR}/db.sqlite3")
        )
    }
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    # STATICFILES_STORAGE = os.getenv("STATICFILES_STORAGE")
    # MEDIA_URL = os.getenv("MEDIA_URL", "/images/")

else:
    DATABASES = {
        "default": dj_database_url.config(
            default=os.getenv("DATABASE_URL", "sqlite://f{BASE_DIR}/db.sqlite3")
        )
    }

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
}

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True


CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = (
    *default_headers,
    "X-Company-Id",
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
# FILE_UPLOAD_PERMISSIONS = 0o640

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "user_django_app.User"

SAFE_DELETE_FIELD_NAME = "deleted_at"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "django_project.pagination.VirtualTruckPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # "DEFAULT_PERMISSION_CLASSES": [
    #     "rest_framework.permissions.DjangoModelPermissions",
    # ],
    "DEFAULT_SCHEMA_CLASS": "django_project.schema_class.SchemaWithCompany",
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "NON_FIELD_ERRORS_KEY": "errors",
    "DEFAULT_RENDERER_CLASSES": (
        "django_project.renderers.CustomORJSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",  # Interface gráfica que o rafinha gosta
    ),
}

SIMPLE_JWT = {
    "TOKEN_OBTAIN_SERIALIZER": "core.user.infra.user_django_app.serializers.CustomTokenObtainPairSerializer",
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=480),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Virtual Truck ",
    "DESCRIPTION": "API para gerenciamento do Virtual Truck, incluindo endpoints e documentação.",
    "VERSION": "1.0.0",
}


TOKEN_EXPIRATION_SECONDS = 1200

CELERY_TIMEZONE = "America/Sao_Paulo"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_RESULT_BACKEND = "rpc://"

EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = os.getenv("EMAIL_PORT", 587)  # pylint: disable=invalid-name
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", True)  # pylint: disable=invalid-name
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "lucasantonete@gmail.com")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "loxe xrdk icwz axgc")


API_VERSION = "v1"
