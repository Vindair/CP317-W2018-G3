from .settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=s@(4^&d5%99caa-=u!3m_#5m6nts(z-r#lh+ht8!kif80c2dt'
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'subby',
        'USER': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'PASSWORD': 'postgres',
        'TEST': {
            'NAME': 'test_subby'
        },
    }
}
