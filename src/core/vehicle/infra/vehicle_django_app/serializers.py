from rest_framework import serializers

from core.uploader.infra.uploader_django_app.serializers import DocumentSerializer
from core.vehicle.infra.vehicle_django_app.models import Body, Modality, Vehicle


class BodyListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)


class BodyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = ["id", "description"]
        read_only_fields = ["id"]


class ModalityListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)
    axle = serializers.IntegerField(read_only=True)


class ModalityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modality
        fields = ["id", "description", "axle"]
        read_only_fields = ["id"]


class VehicleDetailSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    license = serializers.CharField(read_only=True)
    chassis = serializers.CharField(read_only=True)
    renavam = serializers.CharField(read_only=True)
    axle = serializers.IntegerField(read_only=True)
    year = serializers.IntegerField(read_only=True)
    gross_weight = serializers.IntegerField(read_only=True)
    vehicle_type = serializers.CharField(read_only=True)
    body = serializers.UUIDField(source="body_id", read_only=True)
    modality = serializers.UUIDField(source="modality_id", read_only=True)
    documents = DocumentSerializer(many=True, read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class VehicleListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    license = serializers.CharField(read_only=True)
    chassis = serializers.CharField(read_only=True)
    renavam = serializers.CharField(read_only=True)
    vehicle_type = serializers.CharField(read_only=True)
    body = serializers.UUIDField(source="body_id", read_only=True)
    modality = serializers.UUIDField(source="modality_id", read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class VehicleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = [
            "license",
            "chassis",
            "renavam",
            "axle",
            "year",
            "gross_weight",
            "vehicle_type",
            "body",
            "modality",
        ]
        read_only_fields = ["id"]
        extra_kwargs = {
            "license": {"required": True},
        }


class VehicleDocumentSerializer(serializers.Serializer):
    vehicle = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
