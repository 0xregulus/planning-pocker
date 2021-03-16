"""
ASGI config for planningpocker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

from polls.routing import websocket_urlpatterns
from polls.middleware import TokenAuthMiddlewareStack


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planningpocker.settings.local')


application = ProtocolTypeRouter(
    {
        "websocket": TokenAuthMiddlewareStack(
            URLRouter(websocket_urlpatterns)
        ),
    }
)
