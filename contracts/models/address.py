from django.db import models
from contracts.models.base import BaseModel


class Address(BaseModel):
    country = models.CharField(
        max_length=150,
        verbose_name="Country"
    )
    state = models.CharField(
        max_length=150,
        verbose_name="State"
    )
    city = models.CharField(
        max_length=150,
        verbose_name="City"
    )
    neighborhood = models.CharField(
        max_length=150,
        verbose_name="Neighborhood"
    )
    street = models.CharField(
        max_length=150,
        verbose_name="Street"
    )
    number = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Number"
    )
    complement = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Complement"
    )
    postal_code = models.CharField(
        max_length=150,
        verbose_name="Postal code"
    )

    class Meta:
        db_table = "addresses"
        verbose_name = "Address"
        verbose_name_plural = "Addresses"