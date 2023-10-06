from django.urls import path
from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail

urlpatterns = [
    path('polls/', polls_list, name='polls_list'),
    path('polls/<int:id>', polls_detail, name='polls_detail'),

    # URLS routing to the APIView class
    path('apiview_polls/', PollList.as_view(), name='apiview_polls'),
    path('apiview_poll/<int:id>', PollDetail.as_view(), name='apiview_poll'),
]