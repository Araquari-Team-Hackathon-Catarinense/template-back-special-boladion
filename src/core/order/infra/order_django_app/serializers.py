from rest_framework import serializers

from core.order.infra.order_django_app.models import MeasurementUnit, Packing


class MeasurementUnitListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)


class MeasurementUnitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementUnit
        fields = ["id", "description", "company"]
        read_only_fields = ["id"]


class PackingListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)


class PackingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packing
        fields = [
            "id",
            "company",
            "description",
        ]
        read_only_fields = ["id"]
