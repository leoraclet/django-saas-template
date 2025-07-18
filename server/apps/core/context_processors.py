from django.conf import settings


def global_settings(_):
    return {
        "PROJECT_NAME": "PROJECT_NAME",
    }


def allauth_settings(_):
    """Expose some settings from django-allauth in templates."""
    return {
        "ACCOUNT_ALLOW_REGISTRATION": settings.ACCOUNT_ALLOW_REGISTRATION,
    }
