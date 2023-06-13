
from accounts.models import User
from .models import Message,ChatRoom
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async,async_to_sync
from rest_framework.authtoken.models import Token

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #self.user = self.scope["user"]
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print('---------------------------------------------')
        self.room_object=ChatRoom.objects.get(name=self.room_name)
        # Get the token from the query parameters
        token = self.scope['query_string'].decode('utf-8')
        
        # Verify the token and get the user
        try:
            token_obj = Token.objects.get(key=token)
            self.user = token_obj.user
        except Token.DoesNotExist:
            # Close the connection if the token is invalid
            await self.close()




        if not self.user.is_authenticate:
            await self.close()


        # Check if user is the designated user or an admin
        if not self.user.is_staff or (self.room_object.user.name!=self.user.name):
            await self.close()

        name = self.room_name
        self.room_group_name = f'chat_{name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        print('Disconnected')
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Check if user is authenticated and has permission to send messages
        '''if not self.user.is_authenticated or (not self.user.is_staff and self.user.username != "designated_user"):
            await self.close()'''
        
        if not self.user.is_authenticate or not self.user.is_stuff or(self.user.name!=self.room_name):
            await self.close()
        
        # Save message to database
        Message.objects.create(user=self.user, message=message,chat_room=self.room_object)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
