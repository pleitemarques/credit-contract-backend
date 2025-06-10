from typing import Optional
from drf_spectacular.utils import OpenApiParameter, OpenApiTypes, extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from contracts.serializers import ContractSummarySerializer
from contracts.services.summary_service import get_contracts_summary


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="borrower_document",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            required=False
        ),
        OpenApiParameter(
            name="emission_date",
            type=OpenApiTypes.DATE,
            location=OpenApiParameter.QUERY,
            required=False
        ),
        OpenApiParameter(
            name="borrower_state",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            required=False
        )
    ],
    responses={200: ContractSummarySerializer}
)
class ContractSummaryView(APIView):
    def get(self, request: Request) -> Response:
        borrower_document: Optional[str] = request.query_params.get("borrower_document")
        emission_date: Optional[str] = request.query_params.get("emission_date")
        borrower_state: Optional[str] = request.query_params.get("borrower_state")

        summary_data = get_contracts_summary(
            borrower_document=borrower_document,
            emission_date=emission_date,
            borrower_state=borrower_state
        )

        return Response(summary_data, status=status.HTTP_200_OK)