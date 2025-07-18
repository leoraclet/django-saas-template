"""
Base settings to build other settings files upon
"""

import logging
import os
import re
import sys
from pathlib import Path

import apprise
import environ
import sentry_sdk
from corsheaders.defaults import default_headers
from django.utils.translation import gettext_lazy
from loguru import logger
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.loguru import LoggingLevels, LoguruIntegration
from sentry_sdk.integrations.redis import RedisIntegration

env = environ.Env(
    DEBUG=(bool, True),
    STRIPE_LIVE_MODE=(bool, False),
    SECURE=(bool, False),
    SMTP_DEV=(bool, False),
    DOCKER=(bool, False),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR.parent, ".env.dev"))

# ==============================================================================
# SENTRY
# ==============================================================================

# https://docs.sentry.io/platforms/python/guides/django/
sentry_sdk.init(
    dsn=env.str("SENTRY_DSN"),
    _experiments={"enable_logs": True},
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=float(os.environ.get("SENTRY_PROFILES_SAMPLE_RATE", 1.0)),
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
    # The parameter enable_tracing needs to be set when initializing
    # the Sentry SDK for performance measurements to be recorded.
    enable_tracing=True,
    integrations=[
        LoguruIntegration(
            level=LoggingLevels.INFO.value,  # Capture INFO and above as breadcrumbs
            event_level=LoggingLevels.ERROR.value,  # Send ERROR logs as events
            sentry_logs_level=LoggingLevels.INFO.value,  # Capture INFO and above as logs
        ),
        DjangoIntegration(
            cache_spans=True,
        ),
        CeleryIntegration(
            monitor_beat_tasks=True,
        ),
        RedisIntegration(
            max_data_size=None,  # type: ignore
            cache_prefixes=["mycache", "template.cache"],
        ),
    ],
    # Set the environment variable to the environment you are running in
    environment=os.environ.get("SENTRY_ENVIRONMENT", "development"),
    # To collect profiles for all profile sessions,
    # set `profile_session_sample_rate` to 1.0.
    profile_session_sample_rate=1.0,
    # Profiles will be automatically collected while
    # there is an active span.
    profile_lifecycle="trace",
)

# ==============================================================================
# GENERAL
# ==============================================================================

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
INSECURE_KEY = "django-insecure-0eikswwglid=ukts4l2_b=676m!-q_%154%2z@&l3)n6)cp3#c"

# https://docs.djangoproject.com/en/5.0/ref/settings/#secret-key
SECRET_KEY = os.environ.get("SECRET_KEY", INSECURE_KEY)

# https://docs.djangoproject.com/en/5.0/ref/settings/#debug
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG")

# https://docs.djangoproject.com/en/5.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

if os.environ.get("ALLOWED_HOSTS") is not None:
    try:
        ALLOWED_HOSTS += str(os.environ.get("ALLOWED_HOSTS")).split(",")
    except Exception:
        print("Cant set ALLOWED_HOSTS, using default instead")
elif DEBUG:
    ALLOWED_HOSTS += ["localhost", "127.0.0.1", "foo.test"]


# https://django-debug-toolbar.readthedocs.io/en/latest
if DEBUG:
    INTERNAL_IPS = ["127.0.0.1", "localhost", "foo.test"]

    # If using docker, set the internal IP to the docker gateway
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

# ==============================================================================
# Internationalization
# ==============================================================================

# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = "en-us"

# https://docs.djangoproject.com/en/5.0/ref/settings/#languages
LANGUAGES = [
    ("en", gettext_lazy("English")),
    ("fr", gettext_lazy("French")),
]

# https://docs.djangoproject.com/en/5.0/ref/settings/#locale-paths
LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

# https://docs.djangoproject.com/en/5.0/ref/settings/#time-zone
TIME_ZONE = "Europe/Paris"

# https://docs.djangoproject.com/en/5.0/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/5.0/ref/settings/#use-l10n

# https://docs.djangoproject.com/en/5.0/ref/settings/#use-tz
USE_TZ = True

# https://docs.djangoproject.com/en/5.0/ref/settings/#site-id
SITE_ID = 1

# ==============================================================================
# URLS
# ==============================================================================

ADMIN_URL = os.environ.get("ADMIN_URL", "admin/")

# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"

# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# https://docs.djangoproject.com/en/dev/ref/settings/#asgi-application
ASGI_APPLICATION = "config.asgi.application"

# ==============================================================================
# DATABASES
# ==============================================================================

# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

if os.environ.get("DATABASE", "sqlite") == "postgres":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "HOST": os.environ.get("POSTGRES_HOST"),
            "NAME": os.environ.get("POSTGRES_DB"),
            "USER": os.environ.get("POSTGRES_USER"),
            "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
            "PORT": os.environ.get("POSTGRES_PORT"),
            "CONN_MAX_AGE": 600,  # number of seconds database connections should persist for
        }
    }

# https://docs.djangoproject.com/en/5.0/ref/settings/#conn-max-age
CONN_MAX_AGE = None

# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==============================================================================
# APPS
# ==============================================================================

DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.humanize",
    "django.forms",
    # the default admin was replaced by this one
    "config.admin.CustomAdminConfig",
    # "django.contrib.admin",
]

THIRD_PARTY_APPS = [
    # Authentication
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.github",
    "allauth.mfa",
    "allauth.usersessions",
    "allauth.headless",
    "allauth.idp.oidc",
    # REST API
    "rest_framework",
    "rest_framework.authtoken",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "corsheaders",
    # Payments & Subscriptions
    "djstripe",
    # Task scheduler
    "django_celery_beat",
    # Cache
    "cachalot",
]

LOCAL_APPS = [
    "apps.core",
    "apps.users",
]

if DEBUG:
    THIRD_PARTY_APPS += ["silk"]
    THIRD_PARTY_APPS += ["debug_toolbar"]
    THIRD_PARTY_APPS += ["django_browser_reload"]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic", "daphne", *INSTALLED_APPS]

# ==============================================================================
# MIDDLEWARE
# ==============================================================================

# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # CORS middleware -- needs to be placed before Whitenoise or CommonMiddleware
    "corsheaders.middleware.CorsMiddleware",
    # Whitenoise
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # Django's middlewares
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Local middlewares
    # ...
    # Third party middlewares
    "corsheaders.middleware.CorsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "allauth.usersessions.middleware.UserSessionsMiddleware",
]

if DEBUG:
    MIDDLEWARE += ["silk.middleware.SilkyMiddleware"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    MIDDLEWARE += ["django_browser_reload.middleware.BrowserReloadMiddleware"]

# Cache middleware
# https://docs.djangoproject.com/en/5.0/topics/cache/#middleware
MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    *MIDDLEWARE,
    "django.middleware.cache.FetchFromCacheMiddleware",
]
# ==============================================================================
# STORAGES
# ==============================================================================

# https://docs.djangoproject.com/en/5.0/ref/settings/#storages
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# ==============================================================================
# STATIC FILES
# ==============================================================================

# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# ==============================================================================
# MEDIA FILES
# ==============================================================================

# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# ==============================================================================
# TEMPLATES
# ==============================================================================

# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ==============================================================================
# FIXTURES
# ==============================================================================

# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = [
    BASE_DIR / "fixtures",
]

# ==============================================================================
# PASSWORDS
# ==============================================================================

# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
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

if DEBUG:
    AUTH_PASSWORD_VALIDATORS = []

# https://docs.djangoproject.com/en/5.0/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]

# ==============================================================================
# AUTHENTICATION
# ==============================================================================

# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]

# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "/"

# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "/accounts/login/"

# =============================================================================
# SESSIONS
# =============================================================================

# https://docs.djangoproject.com/en/5.0/ref/settings/#session-expire-at-browser-close
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# https://docs.djangoproject.com/en/5.0/ref/settings/#session-cookie-age
SESSION_COOKIE_AGE = 120 * 60

if os.environ.get("REDIS_URL"):
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_CACHE_ALIAS = "default"

# =============================================================================
# CACHE
# =============================================================================

# https://docs.djangoproject.com/en/5.0/topics/cache/
# https://docs.djangoproject.com/en/5.0/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

if os.environ.get("REDIS_URL"):
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": os.environ.get("REDIS_URL"),
        }
    }
elif not DEBUG:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.db.DatabaseCache",
            "LOCATION": "my_cache_table",
        }
    }

# ==============================================================================
# EMAIL
# ==============================================================================

# https://docs.djangoproject.com/en/5.0/topics/email/

# https://docs.djangoproject.com/en/5.0/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# https://docs.djangoproject.com/en/5.0/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = os.environ.get("DJANGO_DEFAULT_FROM_EMAIL")

# https://docs.djangoproject.com/en/5.0/ref/settings/#server-email
SERVER_EMAIL = os.environ.get("DJANGO_SERVER_EMAIL")

# https://docs.djangoproject.com/en/5.0/ref/settings/#email-host
EMAIL_HOST = os.environ.get("DJANGO_EMAIL_HOST")

# https://docs.djangoproject.com/en/5.0/ref/settings/#email-port
EMAIL_PORT = os.environ.get("DJANGO_EMAIL_PORT")

# https://docs.djangoproject.com/en/5.0/ref/settings/#email-host-user
EMAIL_HOST_USER = os.environ.get("DJANGO_EMAIL_HOST_USER")

# https://docs.djangoproject.com/en/5.0/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = os.environ.get("DJANGO_EMAIL_HOST_PASSWORD")

# https://docs.djangoproject.com/en/5.0/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")
SMTP_DEV = env.bool("SMTP_DEV")

if ADMIN_EMAIL is not None:
    ADMINS = [("Admin", ADMIN_EMAIL)]
else:
    ADMINS = [("Admin", "admin@email.com")]

MANAGERS = ADMINS

if DEBUG and SMTP_DEV:
    EMAIL_USE_TLS = False

if DEBUG and not SMTP_DEV:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ==============================================================================
# SECURITY
# ==============================================================================

CSRF_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_SAMESITE = "Strict"
CSRF_COOKIE_HTTPONLY = False  # False since we will grab it via universal-cookies
SESSION_COOKIE_HTTPONLY = True

if DEBUG:
    CSRF_TRUSTED_ORIGINS = [
        "https://foo.test",
    ]

# https://docs.djangoproject.com/en/5.0/topics/security/

if env.bool("SECURE"):
    # https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-name
    SESSION_COOKIE_NAME = "__Secure-sessionid"

    # https://docs.djangoproject.com/en/5.0/ref/settings/#session-cookie-secure
    SESSION_COOKIE_SECURE = True

    # https://docs.djangoproject.com/en/5.0/ref/settings/#session-cookie-httponly
    SESSION_COOKIE_HTTPONLY = True

    # https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-cookie-secure
    CSRF_COOKIE_SECURE = True

    # https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-name
    CSRF_COOKIE_NAME = "__Secure-csrftoken"

    # https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-trusted-origins
    CSRF_TRUSTED_ORIGINS = []

    # https://docs.djangoproject.com/en/5.0/ref/settings/#secure-hsts-include-subdomains
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    # https://docs.djangoproject.com/en/5.0/ref/settings/#secure-hsts-preload
    SECURE_HSTS_PRELOAD = True

    # https://docs.djangoproject.com/en/5.0/ref/settings/#secure-hsts-seconds
    SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 2

    # https://docs.djangoproject.com/en/5.0/ref/settings/#secure-ssl-redirect
    SECURE_SSL_REDIRECT = True

    # https://docs.djangoproject.com/en/5.0/ref/settings/#secure-proxy-ssl-header
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    # https://docs.djangoproject.com/en/5.0/ref/settings/#secure-browser-xss-filter
    SECURE_BROWSER_XSS_FILTER = True

    # https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
    X_FRAME_OPTIONS = "DENY"

    # https://docs.djangoproject.com/en/5.0/ref/settings/#secure-content-type-nosniff
    SECURE_CONTENT_TYPE_NOSNIFF = True

    # https://docs.djangoproject.com/en/5.0/ref/settings/#use-https-in-absolute-urls
    USE_HTTPS_IN_ABSOLUTE_URLS = True

# ==============================================================================
# LOGGING
# =============================================================================

# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# https://docs.djangoproject.com/en/5.0/topics/logging/

# Disable Django's default logging config
# https://docs.djangoproject.com/en/5.0/ref/settings/#logging-config
LOGGING_CONFIG = None


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:  # type: ignore
            frame = frame.f_back  # type: ignore
            depth += 1

        regex = re.compile(r"(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]")
        logger.opt(depth=depth, exception=record.exc_info).log(
            level, regex.sub("", record.getMessage()), colorize=False
        )


# Intercept standard logging
logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)
# Create a logs directory if it doesn't exist
os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="DEBUG", backtrace=True, diagnose=True)
logger.add(
    "logs/debug.log",
    level="DEBUG",
    rotation="30 MB",
    backtrace=True,
    diagnose=True,
    colorize=False,
    retention="7 days",
    enqueue=True,
)

# ==============================================================================
# SILK PROFILER
# ==============================================================================

# https://github.com/jazzband/django-silk

SILKY_META = True
SILKY_PYTHON_PROFILER = False

SILKY_AUTHENTICATION = False
SILKY_AUTHORISATION = False

SILKY_MAX_REQUEST_BODY_SIZE = 1024  # If request body > 1kb, don't log
SILKY_MAX_RESPONSE_BODY_SIZE = 1024  # If response body > 1kb, don't log

# ==============================================================================
# DJANGO ALLAUTH
# ==============================================================================

# https://django-allauth.readthedocs.io/en/latest/installation.html

# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_LOGOUT_REDIRECT_URL = "/"

AUTH_USER_MODEL = "users.User"
# https://docs.allauth.org/en/latest/account/configuration.html
ACCOUNT_ADAPTER = "apps.users.allauth.AccountAdapter"
# https://docs.allauth.org/en/latest/socialaccount/configuration.html
SOCIALACCOUNT_ADAPTER = "apps.users.allauth.SocialAccountAdapter"
# https://docs.allauth.org/en/latest/socialaccount/configuration.html
SOCIALACCOUNT_FORMS = {"signup": "apps.users.forms.UserSocialSignupForm"}
# https://docs.allauth.org/en/latest/account/forms.html
ACCOUNT_FORMS = {"signup": "apps.users.forms.UserSignupForm"}

# https://docs.allauth.org/en/latest/account/configuration.html
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_LOGIN_BY_CODE_ENABLED = True
ACCOUNT_PASSWORD_RESET_BY_CODE_ENABLED = True

MFA_SUPPORTED_TYPES = [
    "webauthn",
    "totp",
    "recovery_codes",
]
MFA_PASSKEY_LOGIN_ENABLED = True
MFA_PASSKEY_SIGNUP_ENABLED = True
ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True

USERSESSIONS_TRACK_ACTIVITY = True

# ==============================================================================
# DJANGO REST FRAMEWORK
# ==============================================================================

# Django REST Framework
# https://www.django-rest-framework.org/#installation

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
}

# https://drf-spectacular.readthedocs.io/en/latest/

SPECTACULAR_SETTINGS = {
    "TITLE": "API_NAME",
    "DESCRIPTION": "API_DESCRIPTION",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    # OTHER SETTINGS
}

# CORS Headers
# https://pypi.org/project/django-cors-headers/

# CORS_URLS_REGEX = r"^/api/.*$"
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:3000",  # Frontend
    "http://localhost",
    "http://127.0.0.1",
    "http://::1",
    "https://foo.test",
]

CORS_ALLOW_HEADERS = (
    *default_headers,
    "x-session-token",
    "x-email-verification-key",
    "x-password-reset-key",
)

# ==============================================================================
# STRIPE
# ==============================================================================

# https://dj-stripe.readthedocs.io/en/stable/

DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"

# Change to True in production
STRIPE_LIVE_MODE = env.bool("STRIPE_LIVE_MODE")

STRIPE_PRICING_TABLE_ID = "prctbl_1RiGUiAbMMYzimnPZ2JUOdiv"
STRIPE_PUBLIC_KEY = "pk_test_51PsuxjAbMMYzimnPntGCoFQJLPsr7gBMZcFHxYwF1MELsGQwRW6yLJYEN9oYg3WJq1jOzO8JqJomJIhQ7AKRZ1rd00eAG62piy"

# ==============================================================================
# CELERY
# ==============================================================================

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-timezone
if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE

if DEBUG and not env.bool("DOCKER"):
    CELERY_TASK_ALWAYS_EAGER = (
        True  # Run tasks synchronously for testing and development
    )

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-task_always_eager
CELERY_TASK_EAGER_PROPAGATES = True

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-broker_url
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-result-backend-settings
CELERY_RESULT_BACKEND = CELERY_BROKER_URL

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#result-extended
CELERY_RESULT_EXTENDED = True

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-task_track_started
CELERY_TASK_TRACK_STARTED = True

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#result-backend-always-retry
# https://github.com/celery/celery/pull/6122
CELERY_RESULT_BACKEND_ALWAYS_RETRY = True

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#result-backend-max-retries
CELERY_RESULT_BACKEND_MAX_RETRIES = 10

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-accept_content
CELERY_ACCEPT_CONTENT = ["json"]

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-task_serializer
CELERY_TASK_SERIALIZER = "json"

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std:setting-result_serializer
CELERY_RESULT_SERIALIZER = "json"

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_TIME_LIMIT = 3600

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-soft-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_SOFT_TIME_LIMIT = 3000

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#beat-scheduler
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#worker-send-task-events
CELERY_WORKER_SEND_TASK_EVENTS = True

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#std-setting-task_send_sent_event
CELERY_TASK_SEND_SENT_EVENT = True

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#worker-hijack-root-logger
CELERY_WORKER_HIJACK_ROOT_LOGGER = False

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#worker-max-memory-per-child
CELERY_WORKER_MAX_MEMORY_PER_CHILD = 200000  # 200MB per worker

# ==============================================================================
# DJANGO DEBUG TOOLBAR
# ==============================================================================

# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.alerts.AlertsPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]

# ==============================================================================
# SVELTE INTEGRATION
# ==============================================================================

VITE_APP_DIR = BASE_DIR.joinpath("frontend")

STATICFILES_DIRS += [VITE_APP_DIR]


# http://whitenoise.evans.io/en/stable/django.html#WHITENOISE_IMMUTABLE_FILE_TEST
def immutable_file_test(_, url):
    # Match vite (rollup)-generated hashes, à la, `some_file-CSliV9zW.js`
    return re.match(r"^.+[.-][0-9a-zA-Z_-]{8,12}\..+$", url)


WHITENOISE_IMMUTABLE_FILE_TEST = immutable_file_test

# ==============================================================================
# HEALTH CHECKS
# ==============================================================================

INSTALLED_APPS += [
    # ...
    "health_check",  # required
    "health_check.db",  # stock Django health checkers
    "health_check.cache",
    "health_check.storage",
    "health_check.contrib.migrations",
    "health_check.contrib.celery",  # requires celery
    "health_check.contrib.psutil",  # disk and memory utilization; requires psutil
    "health_check.contrib.db_heartbeat",
]

# ==============================================================================
# APPRISE
# ==============================================================================

# Define the configuration constants.
WEBHOOK_ID = env.str("WEBHOOK_ID")
WEBHOOK_TOKEN = env.str("WEBHOOK_TOKEN")
TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
TELEGRAM_BOT_CHAT_ID = env.str("TELEGRAM_BOT_CHAT_ID")
NTFY_SHOT = env.str("NTFY_SHOT")
NTFY_TOPIC = env.str("NTFY_TOPIC")

# Prepare the object to send Discord notifications.
notifier = apprise.Apprise()
notifier.add(
    f"discord://{WEBHOOK_ID}/{WEBHOOK_TOKEN}/?image=Yes&footer=Yes&format=markdown"
)
notifier.add(f"ntfy://{NTFY_SHOT}/{NTFY_TOPIC}/?title=Django%20Alert&priority=max")
notifier.add(f"tgram://{TELEGRAM_BOT_TOKEN}/{TELEGRAM_BOT_CHAT_ID}/?format=markdown")

# Install a handler to be alerted on each error.
# You can filter out logs from "apprise" itself to avoid recursive calls.
logger.add(
    sink=notifier.notify,  # type: ignore
    colorize=False,
    backtrace=True,
    diagnose=True,
    level="ERROR",
    filter={"apprise": False},
    enqueue=True,
)
