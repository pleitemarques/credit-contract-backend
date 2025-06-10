from typing import Any, Dict, Optional
from django.db.models import Avg, Count, Sum
from contracts.models import Contract


def get_contracts_summary(
    borrower_document: Optional[str] = None,
    emission_date: Optional[str] = None,
    borrower_state: Optional[str] = None
) -> Dict[str, Any]:
    queryset = Contract.objects.all()

    if borrower_document:
        queryset = queryset.filter(borrower_document=borrower_document)

    if emission_date:
        queryset = queryset.filter(emission_date=emission_date)

    if borrower_state:
        queryset = queryset.filter(borrower_address__state=borrower_state)

    totals = queryset.aggregate(
        total_receivable_amount=Sum("installments__amount"),
        total_disbursed_amount=Sum("amount"),
        total_contracts=Count("id"),
        average_contract_rate=Avg("rate")
    )

    return {
        "total_receivable_amount": totals.get("total_receivable_amount", 0),
        "total_disbursed_amount": totals.get("total_disbursed_amount", 0),
        "total_contracts": totals.get("total_contracts", 0),
        "average_contract_rate": totals.get("average_contract_rate", 0),
    }