from rest_framework import serializers

from core.uploader.infra.uploader_django_app.serializers import DocumentSerializer
from core.vehicle.domain.value_objects import VehicleType
from core.vehicle.infra.vehicle_django_app.models import (
    Body,
    Composition,
    Modality,
    Vehicle,
    VehicleComposition,
)


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
    composition = serializers.UUIDField(source="composition_id", read_only=True)

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


class CompositionListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    axle = serializers.IntegerField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)


class CompositionDetailSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    axle = serializers.IntegerField(read_only=True)
    gross_weight = serializers.IntegerField(read_only=True)
    date = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)


class CompositionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composition
        fields = ["id", "axle", "gross_weight", "date", "is_active"]
        read_only_fields = ["id", "date"]


class VehicleCompositionListSerializer(serializers.Serializer):
    vehicle = serializers.UUIDField(source="vehicle_id", read_only=True)
    composition = serializers.UUIDField(source="composition_id", read_only=True)
    sequence = serializers.IntegerField(read_only=True)


class VechicleCompositionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleComposition
        fields = ["vehicle", "composition", "sequence"]
        read_only_fields = ["id"]

    def validate(self, attrs) -> dict:

        vehicle_data: dict = attrs["vehicle"]
        composition_data: dict = attrs["composition"]
        sequence: dict = attrs["sequence"]

        vehicle: Vehicle = Vehicle.objects.get(id=vehicle_data.id)
        composition: Composition = Composition.objects.get(id=composition_data.id)

        if vehicle.vehicle_type == VehicleType.TRACIONADORA:

            if sequence != 0:
                raise serializers.ValidationError(
                    "A unidade tracionadora deve ter sequence igual a 0."
                )

            tracionadora_exists = VehicleComposition.objects.filter(
                composition=composition,
                vehicle__vehicle_type=VehicleType.TRACIONADORA,
            ).exists()
            if tracionadora_exists:
                raise serializers.ValidationError(
                    "Cada composição pode ter apenas uma unidade tracionadora."
                )

        return attrs
