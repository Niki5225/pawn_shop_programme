from django.db import models


class Value(models.Model):
    value_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    course_of_buying = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    course_of_selling = models.PositiveIntegerField(
        null=False,
        blank=False,
    )
