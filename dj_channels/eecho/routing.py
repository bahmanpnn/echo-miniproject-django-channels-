from django.urls import path

from eecho import consumers

websocket_urlpatterns = [
    path('ws/', consumers.EchoConsumer),
]
