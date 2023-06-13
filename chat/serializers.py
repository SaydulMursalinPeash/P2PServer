from rest_framework import serializers
from rest_framework import response
from .models import *
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name']
class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=ChatRoom
        fields=['name']

class MessageSerializer(serializers.Serializer):
    user=UserSerializer()
    chat_room=ChatRoomSerializer()
    class Meta:
        model=Message
        fields=['message','user','chat_room','time']