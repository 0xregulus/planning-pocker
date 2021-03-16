from django.urls import path

from polls.views import TaskListCreate, VoteListCreate


urlpatterns = [
    path('api/tasks/', TaskListCreate.as_view(), name='tasks'),
    path('api/votes/', VoteListCreate.as_view(), name='votes'),
]
