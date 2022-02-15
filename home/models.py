from django.conf import settings
from django.db import models


class Food(models.Model):
    "Generated Model"
    name = models.BigIntegerField()
    rating = models.IntegerField(
        null=True,
        blank=True,
    )
