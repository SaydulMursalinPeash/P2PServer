from django.db import models
from accounts.models import User
# Create your models here.


class ChatRoom(models.Model):
    name=models.CharField(max_length=300,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='chatroom_user')
    #stuff=models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name='stuff_name')
    def __str__(self):
        return self.user.name



class Message(models.Model):
    message=models.CharField(max_length=3000,null=True,blank=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='message_user')
    chat_room=models.ForeignKey(ChatRoom,on_delete=models.CASCADE,related_name='chat_room_for_message')
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name+' + '+self.chat_room.name  