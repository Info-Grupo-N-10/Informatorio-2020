from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME':'ALQUILERESDB',
        'Trusted_Connection':'yes',
        'HOST': 'localhost\SQLEXPRESS',
        'OPTIONS':{
        	'driver':'SQL Server Native Client 11.0',
        }
    },
}
