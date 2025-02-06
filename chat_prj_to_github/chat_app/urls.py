from django.urls import path
from .views import *

urlpatterns = [
    path('', create_room, name='create_main'),
    path('<str:room_name>/<str:username>/', message_view, name='room')
]