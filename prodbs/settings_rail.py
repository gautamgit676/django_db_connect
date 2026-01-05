from prodbs.settings import *
from decouple import config

SECRET_KEY = config("SECRET_KEY")
ALLOWED_HOSTS = ["djangodbconnect-production.up.railway.app"]
# ALLOWED_HOSTS = ["djangodbconnect-production.up.railway.app"]
CSRF_TRUSTED_ORIGINS = ['https://djangodbconnect-production.up.railway.app']
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

import dj_database_url

from dotenv import load_dotenv
import os

load_dotenv() # take environment variables from .env.

# DATABASES = {
#     "default": {
#         "ENGINE": config("ENGINE"),
#         "NAME": config("DB_NAME", default="railway"),
#         "USER": config("DB_USER", default="postgres"),
#         "PASSWORD": config("DB_PASSWORD", default="zEAQTolZLLCzIcPyGDItQZcJnvdFVOml"),
#         "HOST": config("DB_HOST", default="postgres.railway.internal"),
#         "PORT": config("DB_PORT", default="5432"),
#     }
# }
if os.environ.get("DATABASE_URL"):
    DATABASES = {
        "default": dj_database_url.config(
            conn_max_age=600,
            ssl_require=True,
        )
    }