from django.db import models
from django_extensions.db.models import TimeStampedModel


class Category(TimeStampedModel):
    """
    This Model will store category details.
    """
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories',
                               null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
