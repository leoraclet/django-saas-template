import json
import uuid

from channels.generic.websocket import AsyncWebsocketConsumer
from django.template.loader import render_to_string


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.messages = []
        await super().connect()

    async def receive(self, text_data):
        # our webhook handling code will go here.
        text_data_json = json.loads(text_data)
        message_text = text_data_json["message"]

        self.messages.append(
            {
                "role": "user",
                "content": message_text,
            }
        )

        # show user's message
        user_message_html = render_to_string(
            "chat/ws/chat_message.html",
            {
                "message_text": message_text,
                "is_system": True,
                "message_id": uuid.uuid4().hex,  # and we add an ID
            },
        )

        await self.send(text_data=user_message_html)
        await self.send(text_data=user_message_html)
