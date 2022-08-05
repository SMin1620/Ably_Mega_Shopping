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

answer_list_create = AnswerListCreateViewSet.as_view({
    'get': 'list',
    'post': 'create',
})


urlpatterns = [
    path('', question_list_create, name='question list create'),
    path('<int:question_id>/', question_detail_update_delete, name='question detail'),
    path('<int:question_id>/answer/', answer_list_create, name='answer list create'),
]