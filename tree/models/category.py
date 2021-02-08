from django.db import models
from mptt.models import TreeForeignKey, MPTTModel


class Category(MPTTModel):
    name = models.CharField(max_length=80)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
