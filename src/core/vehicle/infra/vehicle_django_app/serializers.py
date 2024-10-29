from rest_framework import serializers

from core.vehicle.infra.vehicle_django_app.models import Body


class BodyListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)


class BodyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = ["id", "description"]
        read_only_fields = ["id"]
