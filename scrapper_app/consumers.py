import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ScrapperProgressConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "scrappers",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "scrappers",
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', '')

        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def scrapper_message(self, event):
        message = event['message']
        data = event.get('data', {})

        await self.send(text_data=json.dumps({
            'message': message,
            'data': data
        }))
