from rest_framework import serializers

from core.product.infra.product_django_app.models import MeasurementUnit, Packing


class MeasurementUnitListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)
    company = serializers.UUIDField(source="company.id", read_only=True)


class MeasurementUnitDetailSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)
    company = serializers.UUIDField(read_only=True)


class MeasurementUnitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementUnit
        fields = ["id", "description", "company"]
        read_only_fields = ["id"]


class PackingListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    company_id = serializers.UUIDField(source="company.id", read_only=True)
    description = serializers.CharField(read_only=True)


class PackingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packing
        fields = [
            "id",
            "company_id",
            "description",
        ]
        read_only_fields = ["id"]
