from rest_framework.viewsets import ModelViewSet

from core.__seedwork__.domain.exceptions import CompanyNotInHeader
from core.product.infra.product_django_app.models import Product
from core.product.infra.product_django_app.serializers import (
    ProductCreateSerializer,
    ProductListSerializer,
)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        company_id = getattr(self.request, "company_id", None)

        if company_id:
            return Product.objects.filter(company__id=company_id)
        raise CompanyNotInHeader

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProductListSerializer
        return ProductCreateSerializer
