import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "_gMvz9D_sUX1_bDhv8UtQw5rCq-6DZqK2CYF1uP3Nw0")
DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = ["*", ".vercel.app", "localhost", "127.0.0.1"]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = [
    "content-type",
    "x-api-key",
]
INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "rest_framework",
    "bot",
    'corsheaders'
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
]

ROOT_URLCONF = "chatbot_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": []},
    }
]

WSGI_APPLICATION = "chatbot_project.wsgi.application"
ASGI_APPLICATION = "chatbot_project.asgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

GOOGLE_AI_API_KEY = os.environ.get("GOOGLE_AI_API_KEY", "")
CHATBOT_API_KEY = os.environ.get("CHATBOT_API_KEY", "chatbot-secret")
