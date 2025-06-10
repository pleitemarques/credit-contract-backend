from typing import Any, Dict, List
from contracts.models import Address, Contract, Installment


def create_contract_with_nested(
    borrower_address_data: Dict[str, Any],
    installments_data: List[Dict[str, Any]],
    contract_data: Dict[str, Any]
) -> Contract:
    borrower_address = Address.objects.create(**borrower_address_data)

    contract = Contract.objects.create(
        **contract_data,
        borrower_address=borrower_address
    )

    installments = [
        Installment(**data, contract=contract)
        for data in installments_data
    ]

    Installment.objects.bulk_create(installments)

    return contract