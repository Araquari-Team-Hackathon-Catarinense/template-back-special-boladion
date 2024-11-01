from rest_framework import serializers

from core.company.infra.company_django_app.models import Company
from core.product.infra.product_django_app.models import Product


class ProductListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)
    internal_code = serializers.CharField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "description", "internal_code", "is_active", "company"]
        read_only_fields = ["id"]
        extra_kwargs = {"company": {"write_only": True}}
