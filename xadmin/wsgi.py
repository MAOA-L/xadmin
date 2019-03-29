"""
WSGI config for xadmin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)
sys.path.append('/usr/local/apache2/htdocs//xadmin')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xadmin.settings')

application = get_wsgi_application()
