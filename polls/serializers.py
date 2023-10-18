from .models import Poll, Choice, Vote
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(email=validated_data['email'],
                    username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        # Create tokens when a user is created
        Token.objects.create(user=user)
        return user

