from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

from users.views import current_user, UserList


urlpatterns = [
    path('api/token-auth/', obtain_jwt_token, name='token-auth'),
    path('api/current_user/', current_user, name='current-user'),
    path('api/users/', UserList.as_view(), name='users')
]
