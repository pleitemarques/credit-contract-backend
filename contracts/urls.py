from rest_framework.routers import DefaultRouter
from contracts.views.contract_viewset import ContractViewSet

router = DefaultRouter()

router.register(r"contracts", ContractViewSet, basename="contracts")

urlpatterns = router.urls