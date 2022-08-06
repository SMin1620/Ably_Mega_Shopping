from django.urls import path

from qna.views import (
    QuestionListCreateViewSet,
    QuestionDetailUpdateDeleteViewSet,
    AnswerListCreateViewSet,
)


question_list_create = QuestionListCreateViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

question_detail_update_delete = QuestionDetailUpdateDeleteViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

answer_list = AnswerListCreateViewSet.as_view({
    'get': 'list',
})

answer_create = AnswerListCreateViewSet.as_view({
    'post': 'create'
})


urlpatterns = [
    path('', question_list_create, name='question list create'),
    path('<int:question_id>/', question_detail_update_delete, name='question detail'),
    path('<int:question_id>/answer/', answer_list, name='answer list create'),
    path('answer/', answer_create, name='answer create'),
]