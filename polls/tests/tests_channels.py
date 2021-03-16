from django.test import TestCase
from django.urls import re_path

from channels.testing import WebsocketCommunicator
from channels.routing import URLRouter
from channels.db import database_sync_to_async

from polls.consumers import PollConsumer
from polls.tests.utils import create_testing_objects


class PollTests(TestCase):

    def setUp(self):
        self.task, self.user, self.vote = create_testing_objects()

    async def test_connect(self):
        application = URLRouter([
            re_path(r'^testws/(?P<task_id>[\w\.-]+)/$', PollConsumer.as_asgi()),
        ])
        communicator = WebsocketCommunicator(application, f'/testws/{self.task.token}/')
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        message = await communicator.receive_json_from()
        self.assertEqual(message['type'], 'connect')
        self.assertTrue(type(message['payload']) == list)
        await communicator.disconnect()

    async def test_vote(self):
        application = URLRouter([
            re_path(r'^testws/(?P<task_id>\w+)/$', PollConsumer.as_asgi()),
        ])
        communicator = WebsocketCommunicator(application, f'/testws/{self.task.token}/')
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        await communicator.send_json_to({
            'user': self.user.id,
            'task': self.task.id,
            'value': '5',
            'comments': 'New vote'
        })
        message = await communicator.receive_json_from()
        self.assertEqual(message['type'], 'connect')
        await communicator.disconnect()
