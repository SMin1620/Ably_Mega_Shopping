from rest_framework import serializers

from qna.models import Question, Answer
from user.serializers import UserDetailSerializer


class QuestionSerializer(serializers.ModelSerializer):
    """
    질문 시리얼라이저
    """
    class Meta:
        model = Question
        fields = [
            'id',
            'body',
            'is_complete',
            'reg_date',
            'update_date',
            'user',
            'product'
        ]


class QuestionCreateSerializer(serializers.ModelSerializer):
    """
    질문 생성 시리얼라이저
    """
    user = serializers.ReadOnlyField(source='user.nickname')

    class Meta:
        model = Question
        fields = [
            'id',
            'body',
            'is_complete',
            'reg_date',
            'update_date',
            'user',
            'product',
        ]
        extra_kwargs = {
            'body': {'write_only': True},
            'is_complete': {'read_only': True}
        }


class QuestionDetailUpdateDeleteSerializer(serializers.ModelSerializer):
    """
    질문 상세 조회
    수정
    삭제
    """
    class Meta:
        model = Question
        fields = [
            'id',
            'body',
            'is_complete',
            'reg_date',
            'update_date',
            'user',
            'product'
        ]
        extra_kwargs = {
            'body': {'write_only': True},
            'is_complete': {'read_only': True},
            'user': {'read_only': True},
            'product': {'read_only': True}
        }


class AnswerSerializer(serializers.ModelSerializer):
    """
    답변 시리얼라이저
    """
    class Meta:
        model = Answer
        fields = [
            'id',
            'body',
            'reg_date',
            'update_date',
            'user',
            'question',
        ]


class AnswerCreateSerializer(serializers.ModelSerializer):
    """
    답변 생성
    """
    user = serializers.ReadOnlyField(source='user.nickname')

    class Meta:
        model = Answer
        fields = [
            'id',
            'body',
            'reg_date',
            'update_date',
            'user',
            'question'
        ]
        extra_kwargs = {
            'body': {'write_only': True}
        }

