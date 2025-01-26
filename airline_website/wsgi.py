"""
WSGI config for airline_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'airline_website.settings')

# application = get_wsgi_application()


import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'airline_website.airline_website.settings'
)

application = get_wsgi_application()
