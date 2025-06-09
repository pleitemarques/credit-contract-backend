from rest_framework import serializers
from contracts.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address

        fields = [
            "id",
            "country",
            "state",
            "city",
            "neighborhood",
            "street",
            "number",
            "complement",
            "postal_code",
            "created_at",
            "updated_at",
            "is_active"
        ]

        read_only_fields = [
            "created_at",
            "updated_at",
            "is_active"
        ]