from django.db import models


# Create your models here.


class EuroBought(models.Model):
    course_bought = models.PositiveIntegerField(
        default=1.94,
        null=True,
        blank=True,
    )

    quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
    )


class EuroSold(models.Model):
    course_sold = models.PositiveIntegerField(
        default=1.96,
        null=True,
        blank=True,
    )

    quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
    )


class PoundBought(models.Model):
    course_bought = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
    )


class PoundSold(models.Model):
    course_sold = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
    )


class OtherBought(models.Model):
    value_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )

    quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    course_bought = models.PositiveIntegerField(
        null=False,
        blank=False,
    )


class OtherSold(models.Model):
    value_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )

    course_sold = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
    )
