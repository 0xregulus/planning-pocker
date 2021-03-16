from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from polls.tests.utils import create_testing_objects


class TestVotesView(APITestCase):

    def setUp(self):
        self.task, self.user, self.vote = create_testing_objects()
        self.url = reverse('votes')

    def test_list_unauthorized(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        data = response.json()
        self.assertEqual(data['detail'], 'Authentication credentials were not provided.')

    def test_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(type(data) == list)
        for vote in data:
            self.assertEqual(vote['task'], self.task.id)
            self.assertEqual(vote['user'], self.user.id)
            self.assertEqual(vote['username'], self.user.username)
            self.assertEqual(vote['value'], str(self.vote.value))
            self.assertEqual(vote['comments'], self.vote.comments)
            self.assertEqual(vote['created'], self.vote.created.isoformat()[:-6]+'Z')
            self.assertEqual(vote['updated'], self.vote.updated.isoformat()[:-6]+'Z')

    def test_list_filtered(self):
        # user_id
        # task_id
        pass

    def test_create_unauthorized(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        data = response.json()
        self.assertEqual(data['detail'], 'Authentication credentials were not provided.')

    def test_create_missing_fields(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = response.json()
        self.assertTrue(type(data) == dict)
        self.assertEqual(data['task'], ['This field is required.'])
        self.assertEqual(data['user'], ['This field is required.'])
        self.assertEqual(data['value'], ['This field is required.'])

    def test_create_invalid_value(self):
        self.client.force_authenticate(user=self.user)

        payload = {
            'task': self.task.id,
            'user': self.user.id,
            'value': '7',
            'comments': 'This is my vote'
        }

        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = response.json()
        self.assertEqual(data['value'], ['"7" is not a valid choice.'])

    def test_create(self):
        self.client.force_authenticate(user=self.user)

        payload = {
            'task': self.task.id,
            'user': self.user.id,
            'value': '5',
            'comments': 'This is my vote'
        }

        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.json()
        self.assertTrue(type(data) == dict)
        self.assertEqual(data['task'], self.task.id)
        self.assertEqual(data['user'], self.user.id)
        self.assertEqual(data['username'], self.user.username)
        self.assertEqual(data['value'], payload['value'])
        self.assertEqual(data['comments'], payload['comments'])
        self.assertTrue('created' in data)
        self.assertTrue('updated' in data)
