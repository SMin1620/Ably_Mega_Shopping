import re

from django.db import models

from user.models import User
from tag.models import Tag


# Create your models here.
class Market(models.Model):
    name = models.CharField('마켓 이름', max_length=100)
    site_url = models.URLField('마켓 사이트', max_length=100)
    email = models.EmailField('마켓 이메일', max_length=100)
    description = models.TextField('마켓 설명')
    review_point = models.DecimalField('리뷰 포인트', max_digits=2, decimal_places=1, default=0)

    reg_date = models.DateTimeField('생성 날짜', auto_now_add=True)
    update_date = models.DateTimeField('수정 날짜', auto_now=True)

    master = models.OneToOneField(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)

    class Meta:
        db_table = 'market'

    def __str__(self):
        return f'{self.id}, {self.name}, {self.master}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        old_tags = self.tag.all()
        new_tags = self.extract_tag_list()

        delete_tags: list[Tag] = []
        add_tags: list[Tag] = []

        for old_tag in old_tags:
            if not old_tag in new_tags:
                delete_tags.append(old_tag)

        for new_tag in new_tags:
            if not new_tag in old_tags:
                add_tags.append(new_tag)

        for delete_tag in delete_tags:
            self.tag.remove(delete_tag)

        for add_tag in add_tags:
            self.tag.add(add_tag)

    def extract_tag_list(self) -> list[Tag, ...]:
        tag_name_list = re.findall(r'#([a-zA-Z\dㄱ-힣]+)', self.description)
        tag_list = []

        for tag_name in tag_name_list:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)
        return tag_list

