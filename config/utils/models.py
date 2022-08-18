from django.db import models

from django.utils.timezone import now


class SoftDeleteManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        return super().get_queryset().filter(delete_date__isnull=True)


class DeleteManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        return super().get_queryset().filter(delete_date__isnull=False)


class SoftDeleteModel(models.Model):
    delete_date = models.DateTimeField('삭제 날짜', blank=True, null=True, default=None)

    class Meta:
        abstract = True
        db_table = 'soft_delete'

    objects = SoftDeleteManager()
    deleted_objects = DeleteManager()

    def delete(self, using=None, keep_parents=False):
        self.delete_date = now()
        self.save(update_fields=['delete_date'])

    def restore(self):
        self.delete_date = None
        self.save(update_fields=['delete_date'])