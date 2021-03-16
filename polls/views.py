from rest_framework import generics

from polls.models import Task, Vote
from polls.serializers import TaskSerializer, VoteSerializer


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class VoteListCreate(generics.ListCreateAPIView):
    serializer_class = VoteSerializer

    def get_queryset(self):
        queryset = Vote.objects.all()

        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user__id=user_id)

        task_id = self.request.query_params.get('task_id', None)
        if task_id is not None:
            queryset = queryset.filter(task__id=task_id)

        return queryset
