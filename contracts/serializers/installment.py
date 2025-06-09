from rest_framework import serializers
from contracts.models import Installment


class InstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installment

        fields = [
            "id",
            "number",
            "amount",
            "due_date",
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