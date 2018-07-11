from .settings import *

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', '')
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DBNAME', ''),
        'USER': os.environ.get('DBUSER', ''),
        'HOST': os.environ.get('DBHOST', ''),
        'PORT': os.environ.get('DBPORT', ''),
        'PASSWORD': os.environ.get('DBPASS', ''),
    }
}

