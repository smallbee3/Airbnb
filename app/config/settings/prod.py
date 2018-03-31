from .base import *


DEBUG = False
ALLOWED_HOSTS = []
INSTALLED_APPS += [

]

SECRETS_PROD = os.path.join(SECRETS_DIR, 'prod.json')
secrets_prod = json.loads(open(SECRETS_PROD, 'rt').read())
DATABASES = secrets_prod['DATABASES']
