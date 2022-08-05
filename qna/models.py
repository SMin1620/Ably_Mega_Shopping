from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from product.models import Product
from user.models import User


class Question(models.Model):
    body = models.TextField('질문 내용')
    is_complete = models.BooleanField('답변 완료 여부', default=False)

    reg_date = models.DateTimeField('생성 날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정 날짜', auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='questions')

    class Meta:
        db_table = 'question'

    def __str__(self):
        return f'id : {self.id} / product : {self.product} / body : {self.body}'


class Answer(models.Model):
    body = models.TextField('답글 내용')

    reg_date = models.DateTimeField('생성 날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정 날짜', auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='answers')

    class Meta:
        db_table = 'answer'

    def __str__(self):
        return f'user : {self.user} / question : {self.question.id} / answer : {self.body}'
