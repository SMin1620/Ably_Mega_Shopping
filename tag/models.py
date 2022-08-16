from django.db import models


class Tag(models.Model):
    name = models.CharField('태그', max_length=30, unique=True)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.name
