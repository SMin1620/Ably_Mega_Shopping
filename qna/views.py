from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from qna.models import Question, Answer
from qna.serializers import (
    QuestionSerializer,
    QuestionCreateSerializer,
    QuestionDetailUpdateDeleteSerializer,
    AnswerSerializer,
    AnswerCreateSerializer,
    AnswerDetailUpdateDeleteSerializer
)


class QuestionListCreateViewSet(mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                                viewsets.GenericViewSet):
    """
    질문 목록 조회
    생성
    """
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestionSerializer
        else:
            return QuestionCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class QuestionDetailUpdateDeleteViewSet(mixins.RetrieveModelMixin,
                                        mixins.UpdateModelMixin,
                                        mixins.DestroyModelMixin,
                                        viewsets.GenericViewSet):
    """
    질문 상세 조회
    수정
    삭제
    """
    lookup_url_kwarg = 'question_id'

    queryset = Question.objects.all()
    serializer_class = QuestionDetailUpdateDeleteSerializer

    def partial_update(self, request, *args, **kwargs):
        """
        본인 질문 수정
        """
        kwargs['partial'] = True

        return self.update(request, *args, **kwargs)


class AnswerListCreateViewSet(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              viewsets.GenericViewSet):
    """
    답변 리스트 조회
    생성
    """
    queryset = Answer.objects.all()

    def get_queryset(self):
        if self.request.method == 'GET':
            question_id = self.kwargs['question_id']
            return Answer.objects \
                .filter(question_id=question_id) \
                .prefetch_related('user') \
                .all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AnswerSerializer
        else:
            return AnswerCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AnswerDetailUpdateDeleteViewSet(mixins.RetrieveModelMixin,
                                      mixins.UpdateModelMixin,
                                      mixins.DestroyModelMixin,
                                      viewsets.GenericViewSet):
    """
    답변 상세 조회
    수정
    삭제
    """
    lookup_url_kwarg = 'answer_id'

    queryset = Answer.objects.all()
    serializer_class = AnswerDetailUpdateDeleteSerializer

    def partial_update(self, request, *args, **kwargs):
        """
        본인 답변 수정
        """
        kwargs['partial'] = True

        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs['answer_id']
        answer = get_object_or_404(Answer, pk=pk)
        answer.question.is_complete = False
        answer.question.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


