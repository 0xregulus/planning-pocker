from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from rest_framework_jwt.settings import api_settings

from polls.tests.utils import create_testing_objects

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


class TestUsersSignUpView(APITestCase):

    def setUp(self):
        self.task, self.user, self.vote = create_testing_objects()
        self.url = reverse('users')

    def test_get_method_not_allowed(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_method_not_allowed(self):
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_patch_method_not_allowed(self):
        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_signup_missing_fields(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = response.json()
        self.assertTrue(type(data) == dict)
        self.assertEqual(data['username'], ['This field is required.'])
        self.assertEqual(data['password'], ['This field is required.'])

    def test_signup(self):
        payload = {
            'username': 'newuser',
            'password': 'newpassword'
        }
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.json()
        self.assertTrue(type(data) == dict)
        self.assertEqual(data['username'], payload['username'])
        self.assertTrue('id' in data)
        self.assertTrue('token' in data)
        decoded = jwt_decode_handler(data['token'])
        self.assertEqual(data['username'], decoded['username'])
        self.assertEqual(data['id'], decoded['user_id'])


class TestUsersLoginView(APITestCase):

    def setUp(self):
        self.task, self.user, self.vote = create_testing_objects()
        self.url = reverse('token-auth')

    def test_get_method_not_allowed(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_method_not_allowed(self):
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_patch_method_not_allowed(self):
        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_login_missing_fields(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = response.json()
        self.assertTrue(type(data) == dict)
        self.assertEqual(data['username'], ['This field is required.'])
        self.assertEqual(data['password'], ['This field is required.'])

    def test_login_wrong_credentials(self):
        payload = {
            'username': 'wronguser',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = response.json()
        self.assertTrue(type(data) == dict)
        self.assertEqual(data['non_field_errors'], ['Unable to log in with provided credentials.'])

    def test_login(self):
        payload = {
            'username': self.user.username,
            'password': '12qwaszx'
        }
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(type(data) == dict)
        self.assertEqual(data['user']['id'], self.user.id)
        self.assertEqual(data['user']['username'], self.user.username)
        decoded = jwt_decode_handler(data['token'])
        self.assertEqual(data['user']['username'], decoded['username'])
        self.assertEqual(data['user']['id'], decoded['user_id'])
