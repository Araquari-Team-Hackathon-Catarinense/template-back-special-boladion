from rest_framework import serializers

from core.company.infra.company_django_app.serializers import ContractListSerializer

from .models import Operation, Parking, ParkingSector


class ParkingSectorListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)
    sector_type = serializers.CharField(read_only=True)
    qty_slots = serializers.IntegerField(read_only=True)
    contract = ContractListSerializer(read_only=True, allow_null=True)


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
        sector_type = data.get(
            "sector_type", self.instance.sector_type if self.instance else None
        )
        contract = data.get("contract", None)

        # Validação no caso de criação
        if not self.instance:
            if not sector_type:
                raise serializers.ValidationError("Sector Type is required.")
            if sector_type == "CONTRACT" and contract is None:
                raise serializers.ValidationError(
                    "Contract is required for CONTRACT type."
                )
            elif sector_type == "ROTATIVE":
                data["contract"] = None

        # Validação no caso de atualização
        else:
            if "sector_type" in data:
                if sector_type == "CONTRACT" and contract is None:
                    raise serializers.ValidationError(
                        "Contract is required for CONTRACT type."
                    )
                elif sector_type == "ROTATIVE":
                    data["contract"] = None
                elif sector_type not in ("CONTRACT", "ROTATIVE"):
                    raise serializers.ValidationError("Sector Type is invalid.")
            elif "contract" in data:
                if self.instance.sector_type == "ROTATIVE":
                    data["contract"] = None

        return data


class ParkingListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)
    slots = serializers.IntegerField(read_only=True)
    company = serializers.UUIDField(read_only=True, source="company.id")


class ParkingDetailSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    company = serializers.UUIDField(read_only=True, source="company.id")
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
            "company",
        ]
        read_only_fields = ["id", "slots"]


class OperationListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)


class OperationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = [
            "id",
            "name",
            "parking",
        ]
        read_only_fields = ["id"]
