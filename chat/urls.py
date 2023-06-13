from django.urls import path
from .views import *

urlpatterns = [
    path('messages/<room_name>/',RoomMessage.as_view(),name='get_all_message'),
    path('chat-rooms/',AllChatRooms.as_view(),name='get_all_chat_rooms'),
]
