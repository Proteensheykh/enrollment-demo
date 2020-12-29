from .settings import *

#TEST DATABASE

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

#EMAIL BACKEND
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'