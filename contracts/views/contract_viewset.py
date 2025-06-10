from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from contracts.filters import ContractFilterSet
from contracts.models import Contract
from contracts.serializers import ContractSerializer


class ContractViewSet(viewsets.ModelViewSet):
    queryset = (
        Contract.objects
        .select_related("borrower_address")
        .prefetch_related("installments")
    )

    serializer_class = ContractSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = ContractFilterSet

    search_fields = [
        "external_id",
        "borrower_document",
        "borrower_address__city"
    ]

    ordering_fields = [
        "emission_date",
        "amount",
        "created_at"
    ]

    ordering = ["-created_at"]