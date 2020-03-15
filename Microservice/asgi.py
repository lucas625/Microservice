# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Project asgi module"""

import os

from django.core.asgi import get_asgi_application


os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'Microservice.settings'
)

application = get_asgi_application()
