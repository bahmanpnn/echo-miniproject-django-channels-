from django.urls import path
from dj_channels.eecho import consumers

websocket_urlpatterns = [
    path('ws/', consumers.EchoConsumer),
]
