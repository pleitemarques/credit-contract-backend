from rest_framework import serializers


class ContractSummarySerializer(serializers.Serializer):
    total_receivable_amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    total_disbursed_amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    total_contracts = serializers.IntegerField()
    average_contract_rate = serializers.DecimalField(max_digits=5, decimal_places=2)