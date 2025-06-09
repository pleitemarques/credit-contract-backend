import django_filters
from contracts.models import Contract


class ContractFilterSet(django_filters.FilterSet):
    emission_date = django_filters.DateFilter()

    emission_date__year = django_filters.NumberFilter(
        field_name="emission_date",
        lookup_expr="year"
    )

    emission_date__month = django_filters.NumberFilter(
        field_name="emission_date",
        lookup_expr="month"
    )

    emission_date__day = django_filters.NumberFilter(
        field_name="emission_date",
        lookup_expr="day"
    )

    class Meta:
        model = Contract

        fields = {
            "external_id": ["exact"],
            "borrower_document": ["exact"],
            "borrower_address__state": ["exact"]
        }