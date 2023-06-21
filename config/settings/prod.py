from .base import *

import environ

ALLOWED_HOSTS = ["15.165.115.243", "petemotiondiary.site"]
STATIC_ROOT = BASE_DIR / "static/"
STATICFILES_DIRS = []
DEBUG = False

env = environ.Env()
environ.Env.read_env(BASE_DIR / ".env")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": "3306",
    }
}
