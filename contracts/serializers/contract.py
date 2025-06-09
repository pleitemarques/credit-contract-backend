from datetime import date
from typing import Any, Dict
from rest_framework import serializers
from contracts.models import Contract
from contracts.serializers.address import AddressSerializer
from contracts.serializers.installment import InstallmentSerializer
from contracts.services.contract_service import create_contract_with_nested
from contracts.validators.cpf import is_valid_cpf
from contracts.validators.phone import is_valid_international_phone


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

    def validate_amount(
        self,
        value: float
    ) -> float:
        if value < 0:
            raise serializers.ValidationError(
                "Ensure this value is greater than or equal to 0."
            )

        return value

    def validate_rate(
        self,
        value: float
    ) -> float:
        if value < 0:
            raise serializers.ValidationError(
                "Ensure this value is greater than or equal to 0."
            )

        if value > 100:
            raise serializers.ValidationError(
                "Ensure this value is less than or equal to 100."
            )

        return value

    def validate_emission_date(
        self,
        value: date
    ) -> date:
        if value > date.today():
            raise serializers.ValidationError(
                "Ensure this date is not in the future."
            )

        return value

    def validate_borrower_birthdate(
        self,
        value: date
    ) -> date:
        if value > date.today():
            raise serializers.ValidationError(
                "Ensure this date is not in the future."
            )

        return value

    def validate_borrower_document(
        self,
        value: str
    ) -> str:
        if not value.isdigit() or len(value) != 11:
            raise serializers.ValidationError(
                "Ensure this field has 11 numeric digits."
            )

        if not is_valid_cpf(value):
            raise serializers.ValidationError(
                "Enter a valid document."
            )

        return value

    def validate_borrower_phone(
        self,
        value: str
    ) -> str:
        if not value.isdigit():
            raise serializers.ValidationError(
                "Ensure this field contains only numeric digits."
            )

        if not is_valid_international_phone(value):
            raise serializers.ValidationError(
                "Enter a valid phone."
            )

        return value

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