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

    def validate(self, attrs):
        if "internal_code" not in attrs:
            return super().validate(attrs)
        elif attrs["internal_code"]:
            if attrs["company"]:
                company = Company.objects.get(id=attrs["company"].id)
            else:
                company = self.instance.company
            internal_code_exists = company.products.filter(
                internal_code=attrs["internal_code"]
            )
            if len(internal_code_exists) > 0:
                raise serializers.ValidationError(
                    "Já existe um produto com esse códico"
                )
        return super().validate(attrs)
