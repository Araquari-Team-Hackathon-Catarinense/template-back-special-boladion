from rest_framework import serializers

from .models import Parking, ParkingSector


class ParkingSectorListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)
    sector_type = serializers.CharField(read_only=True)
    qty_slots = serializers.IntegerField(read_only=True)
    contract = serializers.IntegerField(read_only=True, allow_null=True)
    # contract = serializers.UUIDField(read_only=True, allow_null=True, source="contract.id")


class ParkingSectorCreateSerializer(serializers.ModelSerializer):
    contract = serializers.IntegerField(required=False, allow_null=True)

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
        if not self.instance:
            if "sector_type" not in data:
                raise serializers.ValidationError("Sector Type is required")
            if data["sector_type"] == "CONTRACT":
                if "contract" not in data or data["contract"] is None:
                    raise serializers.ValidationError("Contract is required")
            elif data["sector_type"] == "ROTATIVE":
                data["contract"] = None
            else:
                raise serializers.ValidationError("Sector Type is invalid")

        else:
            if "sector_type" in data:
                print(data["sector_type"])
                if data["sector_type"] == "CONTRACT":
                    if "contract" not in data or data["contract"] is None:
                        raise serializers.ValidationError("Contract is required")
                    else:
                        return data
                elif data["sector_type"] == "ROTATIVE":
                    data["contract"] = None
                    return data
                else:
                    raise serializers.ValidationError("Sector Type is invalid")
            elif "contract" in data:
                if self.instance.sector_type == "CONTRACT":
                    return data
                else:
                    data["contract"] = None
                    return data
            else:
                return data
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
