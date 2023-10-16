from django.urls import path
from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, PollViewSet, UserCreate
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollViewSet)

urlpatterns = [
    path('polls/', polls_list, name='polls_list'),
    path('polls/<int:id>', polls_detail, name='polls_detail'),

    # URLS routing to the APIView class
    # path('apiview_polls/', PollList.as_view(), name='apiview_polls'),
    # path('apiview_poll/<int:id>', PollDetail.as_view(), name='apiview_poll'),
    # path('choices/', ChoiceList.as_view(), name='choice_list'),
    # path('vote/', CreateVote.as_view(), name='create_vote'),

    path('polls/<int:id>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:id>/choices/<int:choice_id>/vote', CreateVote.as_view(),  name='create_vote'),

    path('users/', UserCreate.as_view(), name='user_create'),
]

urlpatterns += router.urls

