from typing import Any, Dict
from rest_framework import serializers
from contracts.models import Contract
from contracts.serializers.address import AddressSerializer
from contracts.serializers.installment import InstallmentSerializer
from contracts.services.contract_service import create_contract_with_nested


class ContractSerializer(serializers.ModelSerializer):
    borrower_address = AddressSerializer()
    installments = InstallmentSerializer(many=True)

    class Meta:
        model = Contract

        fields = [
            "id",
            "external_id",
            "emission_date",
            "amount",
            "rate",
            "borrower_document",
            "borrower_birthdate",
            "borrower_phone",
            "borrower_address",
            "installments",
            "created_at",
            "updated_at",
            "is_active"
        ]

        read_only_fields = [
            "created_at",
            "updated_at",
            "is_active"
        ]

    def create(
        self,
        validated_data: Dict[str, Any]
    ) -> Contract:
        borrower_address_data = validated_data.pop("borrower_address")
        installments_data = validated_data.pop("installments")

        return create_contract_with_nested(
            borrower_address_data,
            installments_data,
            validated_data
        )