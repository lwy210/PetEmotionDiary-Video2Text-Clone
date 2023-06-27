from .base import *

import environ

ALLOWED_HOSTS = ["15.165.115.243", "petemotiondiary.site", "127.0.0.1"]

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
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

AWS_ACCESS_KEY_ID = env("S3_KEY")
AWS_SECRET_ACCESS_KEY = env("S3_SECRET_KEY")
AWS_REGION = "ap-northeast-2"

AWS_STORAGE_BUCKET_NAME = "ped-bucket1"
AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (AWS_STORAGE_BUCKET_NAME, AWS_REGION)

STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"

DEFAULT_FILE_STORAGE = "config.settings.storages.S3DefaultStorage"
STATICFILES_STORAGE = "config.settings.storages.S3StaticStorage"
