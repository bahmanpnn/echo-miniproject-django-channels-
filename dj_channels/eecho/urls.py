from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home-page'),
    path('image/', echo_image, name='image-page'),
]
