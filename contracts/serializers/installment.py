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