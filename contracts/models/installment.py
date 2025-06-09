from django.db import models
from contracts.models.base import BaseModel
from contracts.models.contract import Contract


class Installment(BaseModel):
    contract = models.ForeignKey(
        to=Contract,
        on_delete=models.CASCADE,
        related_name="installments",
        verbose_name="Contract"
    )
    number = models.PositiveIntegerField(
        verbose_name="Number"
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Amount"
    )
    due_date = models.DateField(
        verbose_name="Due date"
    )

    class Meta:
        db_table = "installments"
        verbose_name = "Installment"
        verbose_name_plural = "Installments"