from .settings import *
import os

 

# ... otras configuraciones si las tienes ...

 

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.mysql',

        'NAME': 'blogdb',

        'USER': 'root',

        'PASSWORD': 'root',

        'HOST': '127.0.0.1',

        'PORT': '3306',

    }

}

 

# Configura la clave secreta de forma segura

#SECRET_KEY = os.environ.get('SECRET_KEY')