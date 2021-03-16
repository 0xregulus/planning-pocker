from rest_framework import serializers
from polls.models import Task, Vote


class TaskSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'
        read_only = ['id', 'created', 'updated']

    def get_score(self, task):
        return str(task.score)

class VoteSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Vote
        exclude = ['id',]
        read_only = ['created', 'updated']

    def get_username(self, vote):
        return vote.user.username

    def create(self, validated_data):
        vote, created = Vote.objects.update_or_create(
            task=validated_data.get('task'),
            user=validated_data.get('user'),
            defaults={
                'value': validated_data.get('value'),
                'comments': validated_data.get('comments')
            }
        )

        return vote
