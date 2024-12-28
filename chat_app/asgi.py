"""
ASGI config for chat_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import chats.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat_app.settings")

# application = ProtocolTypeRouter(
#     {
#         # Django's ASGI application to handle traditional HTTP requests
#         "http": get_asgi_application(),
#         # WebSocket chat handler
#         "websocket": AuthMiddlewareStack(
#             URLRouter(chats.routing.websocket_urlpatterns)
#         ),
#     }
# )

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(chats.routing.websocket_urlpatterns)
        ),
    }
)
