from secrets import token_urlsafe
from fractions import Fraction

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


def generate_token(nbytes=5):
    """Generate unique token for room."""
    return token_urlsafe(nbytes)


class Task(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField()
    token = models.CharField(max_length=16, default=generate_token, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __rep__(self):
        return f'{self.name}({self.token})'

    def __str__(self):
        return f'{self.name}({self.token})'

    @property
    def score(self):
        votes = self.votes.values_list('value', flat=True)
        if not votes:
            return '?'

        votes = [Fraction(v) for v in votes if v != '?']
        return (sum(votes) / len(votes)) if votes else '?'


class Vote(models.Model):

    VOTE_CHOICES = (
        ('?', '?'),
        ('1/2', '1/2'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('5', '5'),
        ('8', '8'),
        ('13', '13'),
    )

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    task = models.ForeignKey(Task, related_name='votes', on_delete=models.PROTECT)
    value = models.CharField(max_length=3, choices=VOTE_CHOICES)
    comments = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __rep__(self):
        return f'{self.user}: {self.value} @ {self.task}'

    def __str__(self):
        return f'{self.user}: {self.value} @ {self.task}'
