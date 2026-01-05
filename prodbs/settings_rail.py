from prodbs.settings import *
from decouple import config

SECRET_KEY = config("SECRET_KEY")
ALLOWED_HOSTS = ["djangodbconnect-production.up.railway.app"]
# ALLOWED_HOSTS = ["djangodbconnect-production.up.railway.app"]
CSRF_TRUSTED_ORIGINS = ['https://djangodbconnect-production.up.railway.app']
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
