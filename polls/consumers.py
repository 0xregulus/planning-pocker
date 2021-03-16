import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async

from polls.models import Vote
from polls.serializers import VoteSerializer


class PollConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.task_id = self.scope["url_route"]["kwargs"]["task_id"]
        self.group_name = "poll_%s" % self.task_id

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        votes = await self.get_votes()
        await self.send_json({
            'type': 'connect',
            'payload': votes
        })

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    @database_sync_to_async
    def get_votes(self):
        votes = Vote.objects.filter(task__token=self.task_id)
        serializer = VoteSerializer(votes, many=True)
        return serializer.data

    @database_sync_to_async
    def save_vote(self, raw_data):
        serializer = VoteSerializer(data=raw_data)
        if serializer.is_valid():
            vote = serializer.save()
            return VoteSerializer(vote).data

        return serializer.errors

    async def receive_json(self, content):
        vote = await self.save_vote(content)

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'new_vote',
                'payload': vote
            }
        )

    async def new_vote(self, event):
        vote = event['payload']

        await self.send_json({
            'type': 'new_vote',
            'payload': vote
        })
