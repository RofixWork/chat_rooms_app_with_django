# chat/consumers.py
import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from userauths.models import User

from .models import ChatMessage, ChatRoom


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # اسم غرفة الدردشة
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # الانضمام إلى مجموعة WebSocket
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # مغادرة المجموعة عند فصل الاتصال
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        username = data["username"]
        room = data["room"]
        avatar = data["avatar"]
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "send_message",
                "message": message,
                "username": username,
                "room": room,
                "avatar": avatar,
            },
        )
        await self.save_message(message, username, room)

    async def send_message(self, event):
        message = event["message"]
        username = event["username"]
        room = event["room"]
        avatar = event["avatar"]
        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "username": username,
                    "room": room,
                    "avatar": avatar,
                }
            )
        )

    @sync_to_async
    def save_message(self, message, username, room_slug):
        user = User.objects.get(username=username)
        room = ChatRoom.objects.get(slug=room_slug)
        ChatMessage.objects.create(room=room, user=user, message=message)
