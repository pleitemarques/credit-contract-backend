from django.db import models
from contracts.models.address import Address
from contracts.models.base import BaseModel


class Contract(BaseModel):
    external_id = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="External id"
    )
    emission_date = models.DateField(
        verbose_name="Emission date"
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Amount"
    )
    rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Rate"
    )
    borrower_document = models.CharField(
        max_length=11,
        verbose_name="Borrower document"
    )
    borrower_birthdate = models.DateField(
        verbose_name="Borrower birthdate"
    )
    borrower_phone = models.CharField(
        max_length=15,
        verbose_name="Borrower phone"
    )
    borrower_address = models.OneToOneField(
        to=Address,
        on_delete=models.CASCADE,
        related_name="+",
        verbose_name="Borrower address"
    )

    class Meta:
        db_table = "contracts"
        verbose_name = "Contract"
        verbose_name_plural = "Contracts"