from typing import Any, Dict, Optional
from django.db.models import Avg, Count, Sum
from contracts.models import Contract, Installment


def get_contracts_summary(
    borrower_document: Optional[str] = None,
    emission_date: Optional[str] = None,
    borrower_state: Optional[str] = None
) -> Dict[str, Any]:
    contract_queryset = Contract.objects.all()

    if borrower_document:
        contract_queryset = contract_queryset.filter(borrower_document=borrower_document)

    if emission_date:
        contract_queryset = contract_queryset.filter(emission_date=emission_date)

    if borrower_state:
        contract_queryset = contract_queryset.filter(borrower_address__state=borrower_state)

    contract_ids = contract_queryset.values_list("id", flat=True)

    installment_queryset = Installment.objects.filter(contract_id__in=contract_ids)

    installment_totals = installment_queryset.aggregate(
        total_receivable_amount=Sum("amount")
    )

    contract_totals = contract_queryset.aggregate(
        total_disbursed_amount=Sum("amount"),
        total_contracts=Count("id"),
        average_contract_rate=Avg("rate")
    )

    return {
        "total_receivable_amount": installment_totals.get("total_receivable_amount", 0),
        "total_disbursed_amount": contract_totals.get("total_disbursed_amount", 0),
        "total_contracts": contract_totals.get("total_contracts", 0),
        "average_contract_rate": contract_totals.get("average_contract_rate", 0),
    }