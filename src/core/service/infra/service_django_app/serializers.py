from rest_framework import serializers

from core.service.infra.service_django_app.models import Service


class ServiceListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)
    payment_rules = serializers.JSONField(read_only=True)
    parking = serializers.CharField(read_only=True, source="parking.description")


class ServiceCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ["id", "description", "payment_rules", "parking"]
        read_only_fields = ["id"]
