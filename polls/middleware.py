from urllib.parse import parse_qs

from django.contrib.auth import get_user_model

from rest_framework_jwt.utils import jwt_decode_handler

from channels.db import database_sync_to_async
from channels.auth import AuthMiddlewareStack

User = get_user_model()


class TokenAuthMiddleware:

    def __init__(self, inner):
        self.inner = inner

    @database_sync_to_async
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return AnonymousUser()

    async def __call__(self, scope, receive, send):
        try:
            token = parse_qs(scope['query_string'].decode('utf-8'))['token'][0]
            decoded_data = jwt_decode_handler(token)
            scope['user'] = await self.get_user(decoded_data['username'])
        except Exception as e:
            print('==== Exception', e)
            return None

        return await self.inner(scope, receive, send)

TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))
