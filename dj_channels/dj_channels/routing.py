from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from dj_channels.eecho import routing as eecho_routing
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            eecho_routing.websocket_urlpatterns
        )
    )
})
