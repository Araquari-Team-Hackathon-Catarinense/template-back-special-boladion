from rest_framework import serializers

from .models import Parking, ParkingSector


class ParkingSectorListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)
    sector_type = serializers.CharField(read_only=True)
    qty_slots = serializers.IntegerField(read_only=True)


class ParkingSectorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSector
        fields = [
            "id",
            "description",
            "qty_slots",
            "sector_type",
            "parking",
            "contract",
        ]
        read_only_fields = ["id", "slots"]

    def validate(self, data):
        if data["sector_type"] == "CONTRACT":
            if "contract" not in data or data["contract"] is None:
                raise serializers.ValidationError("Contract is required")

        data["contract"] = None
        return data


class ParkingListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)
    slots = serializers.IntegerField(read_only=True)
    entity = serializers.UUIDField(read_only=True, source="entity.id")


class ParkingDetailSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    entity = serializers.UUIDField(read_only=True, source="entity.id")
    description = serializers.CharField(read_only=True)
    slots = serializers.IntegerField(read_only=True)
    sectors = ParkingSectorListSerializer(many=True, read_only=True)


class ParkingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = [
            "id",
            "description",
            "slots",
            "entity",
        ]
        read_only_fields = ["id", "slots"]
