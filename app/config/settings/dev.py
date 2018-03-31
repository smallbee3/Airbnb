from .base import *


DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS += [
    'django_extensions',
]

SECRETS_DEV = os.path.join(SECRETS_DIR, 'dev.json')
secrets_dev = json.loads(open(SECRETS_DEV, 'rt').read())
# DATABASES = secrets_dev['DATABASES']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

