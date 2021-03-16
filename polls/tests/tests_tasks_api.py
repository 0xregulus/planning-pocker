from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from polls.tests.utils import create_testing_objects


class TestTasksView(APITestCase):

    def setUp(self):
        self.task, self.user, self.vote = create_testing_objects()
        self.url = reverse('tasks')

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
        for task in data:
            self.assertEqual(task['name'], self.task.name)
            self.assertEqual(task['description'], self.task.description)
            self.assertEqual(task['score'], str(self.task.score))
            self.assertEqual(task['token'], self.task.token)
            self.assertEqual(task['created'], self.task.created.isoformat()[:-6]+'Z')
            self.assertEqual(task['updated'], self.task.updated.isoformat()[:-6]+'Z')

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
        self.assertEqual(data['name'], ['This field is required.'])
        self.assertEqual(data['description'], ['This field is required.'])

    def test_create(self):
        self.client.force_authenticate(user=self.user)

        payload = {
            'name': 'New Task',
            'description': 'New task created for testing'
        }

        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.json()
        self.assertTrue(type(data) == dict)
        self.assertEqual(data['name'], payload['name'])
        self.assertEqual(data['description'], payload['description'])
        self.assertEqual(data['score'], '?')
        self.assertTrue('token' in data)
        self.assertTrue('created' in data)
        self.assertTrue('updated' in data)
