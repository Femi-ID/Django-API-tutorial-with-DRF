from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Poll
# Create your views here.


def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {'results': list(polls.values('question', 'created_by', 'pub_date'))}
    return JsonResponse(data)
    # A JsonResponse is a like HttpResponse with content-type=application/json.


def polls_detail(request, id):
    poll = get_object_or_404(Poll, id=id)
    data = {'results': {
        'question': poll.question,
        'created_by': poll.created_by.username,
        'pub_date': poll.pub_date
    }}
    return JsonResponse(data)

