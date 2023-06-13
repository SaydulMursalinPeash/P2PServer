from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .renderers import *
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Max
from .renderers import *

class RoomMessage(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request,room_name,fromat=None):
        if request.user.name!=room_name:
            return Response({'error':'You are not allowed to view this chats.'},status=status.HTTP_400_BAD_REQUEST)
        try:
            room=ChatRoom.objects.get(name=room_name)
            messages=room.messages.all()
            serializer=MessageSerializer(messages,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            return Response({'error':'Invalid chat.'},status=status.HTTP_400_BAD_REQUEST)


def get_chat_rooms_ordered_by_last_message_time():
    # Get all the ChatRoom objects
    chat_rooms = ChatRoom.objects.all()

    # Annotate each ChatRoom object with the timestamp of its latest message
    chat_rooms = chat_rooms.annotate(last_message_time=Max('chat_room_for_message__time'))

    # Sort the ChatRoom objects by their latest message timestamp in descending order
    chat_rooms = chat_rooms.order_by('-last_message_time')

    return chat_rooms

class AllChatRooms(APIView):
    permission_classes=[IsAuthenticated,IsAdminUser]
    renderer_classes=[UserRenderer]
    def get(self,request,fromat=None):
        ordered_chatrooms=get_chat_rooms_ordered_by_last_message_time()
        serializer=ChatRoomSerializer(ordered_chatrooms,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


        