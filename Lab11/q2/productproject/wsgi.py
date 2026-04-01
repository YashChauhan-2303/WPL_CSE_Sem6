"""
WSGI config for productproject project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'productproject.settings')

application = get_wsgi_application()
