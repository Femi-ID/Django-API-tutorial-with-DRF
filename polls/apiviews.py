from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer, UserSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets

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

# class ChoiceList(generics.ListCreateAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer

# class CreateVote(generics.CreateAPIView):
#     serializer_class = VoteSerializer


class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll=self.kwargs['id'])
        return queryset
    serializer_class = ChoiceSerializer


class CreateVote(APIView):
    serializer_class = VoteSerializer

    def post(self, request, id, choice_id):
        voted_by = request.data.get('voted_by')
        data = {'choice': choice_id, 'poll': id, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Using viewsets.ModelViewSet
class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer

