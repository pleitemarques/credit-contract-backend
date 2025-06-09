from django.urls import path
from rest_framework.routers import DefaultRouter
from contracts.views.contract_viewset import ContractViewSet
from contracts.views.summary_view import ContractSummaryView

router = DefaultRouter()

router.register(r"contracts", ContractViewSet, basename="contracts")

urlpatterns = [
    path("contracts/summary/", ContractSummaryView.as_view(), name="summary"),
]

urlpatterns += router.urls