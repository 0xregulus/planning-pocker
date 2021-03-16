from django.contrib.auth import get_user_model

from polls.models import Task, Vote

User = get_user_model()


def create_testing_objects():
    task, created = Task.objects.get_or_create(
        name='Testing task',
        description='Testing task description'
    )
    user = User.objects.create_user(
        username='testing',
        password='12qwaszx'
    )
    vote, created = Vote.objects.get_or_create(
        user=user,
        task=task,
        value='5',
        comments='This task is a must!'
    )

    return task, user, vote
