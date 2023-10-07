from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer
from rest_framework import status
from rest_framework import generics


# class PollList(APIView):
#     def get(self, request):
#         polls = Poll.objects.all()
#         # data = PollSerializer(polls, many=True).data
#         serializer = PollSerializer(polls, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class PollDetail(APIView):
#     def get(self, request, id):
#         poll = get_object_or_404(Poll, id=id)
#         # data =PollSerializer(poll)
#         serializer = PollSerializer(poll)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveUpdateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

