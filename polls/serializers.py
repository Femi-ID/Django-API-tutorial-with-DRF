from .models import Poll, Choice, Vote
from rest_framework import serializers

"""Serialization is the process of making a streamable 
representation of the data which we can transfer over the network."""


class VoteSerializer(serializers.Serializer):
    class Meta:
        model = Vote
        fields = '__all__'


class PollSerializer(serializers.Serializer):
    class Meta:
        model = Poll
        fields = '__all__'


class ChoiceSerializer(serializers.Serializer):
    class Meta:
        model = Choice
        fields = '__all__'