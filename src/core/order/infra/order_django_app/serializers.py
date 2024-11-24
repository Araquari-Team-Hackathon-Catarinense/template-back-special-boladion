from rest_framework import serializers

from core.company.infra.company_django_app.models import Contract
from core.order.infra.order_django_app.models import (
    MeasurementUnit,
    Packing,
    PurchaseSaleOrder,
    TransportContract,
    Trip,
)


class MeasurementUnitListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class MeasurementUnitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementUnit
        fields = ["id", "description", "company"]
        read_only_fields = ["id"]
        extra_kwargs = {"company": {"write_only": True}}


class PackingListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    description = serializers.CharField(read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class PackingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packing
        fields = [
            "id",
            "company",
            "description",
        ]
        read_only_fields = ["id"]
        extra_kwargs = {"company": {"write_only": True}}


class PurchaseSaleOrderListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    client = serializers.CharField(source="client.name", read_only=True)
    operation_terminal = serializers.CharField(
        source="operation_terminal.name", read_only=True
    )
    product = serializers.CharField(source="product.description", read_only=True)
    measurement_unit = serializers.CharField(
        source="measurement_unit.description", read_only=True
    )
    packing = serializers.CharField(source="packing.description", read_only=True)
    quantity = serializers.FloatField(read_only=True)
    balance = serializers.FloatField(read_only=True)
    operation_type = serializers.CharField(read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class PurchaseSaleOrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseSaleOrder
        fields = [
            "id",
            "company",
            "client",
            "product",
            "measurement_unit",
            "packing",
            "quantity",
            "operation_terminal",
            "operation_type",
        ]
        read_only_fields = ["id"]
        extra_kwargs = {"company": {"write_only": True}}

    def validate(self, attrs) -> dict:
        company = attrs.get("company")
        client = attrs.get("client")
        operation_terminal = attrs.get("operation_terminal")

        errors = list()

        if not Contract.objects.filter(
            source_company=company, target_company=client, contract_type="CLIENTE"
        ).exists():
            errors.append(
                {
                    "client": "O cliente deve ser uma empresa com um contrato do tipo CLIENTE com a empresa fornecedora.",
                }
            )

        if not (
            Contract.objects.filter(
                contract_type="TERMINAL",
                target_company=operation_terminal,
            )
            .filter(source_company=company)
            .exists()
            or Contract.objects.filter(
                contract_type="TERMINAL",
                source_company=operation_terminal,
            )
            .filter(target_company=client)
            .exists()
            or operation_terminal in [company, client]
        ):
            errors.append(
                {
                    "operation_terminal": "O terminal de operação deve ser uma empresa com um contrato do tipo TERMINAL com a empresa fornecedora ou com o cliente ou ser a própria empresa fornecedora ou cliente.",
                }
            )

        if errors:
            raise serializers.ValidationError(errors)

        return attrs


class TransportContractListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    company = serializers.CharField(source="company.id", read_only=True)
    carrier = serializers.CharField(source="carrier.id", read_only=True)
    purchase_sale_order = serializers.CharField(
        source="purchase_sale_order.id", read_only=True
    )
    balance = serializers.FloatField(read_only=True)
    quantity = serializers.FloatField(read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class TransportContractCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportContract
        fields = [
            "id",
            "company",
            "carrier",
            "purchase_sale_order",
            "balance",
            "quantity",
        ]
        read_only_fields = ["id"]

    def validate(self, attrs) -> dict:
        company = attrs.get("company")
        carrier = attrs.get("carrier")
        purchase_sale_order = attrs.get("purchase_sale_order")

        if not Contract.objects.filter(
            source_company=company,
            target_company=carrier,
            contract_type="TRANSPORTADORA",
        ).exists():
            raise serializers.ValidationError(
                [
                    {
                        "carrier": "A transportadora deve ser uma empresa com um contrato do tipo TRANSPORTADORA com a empresa fornecedora."
                    }
                ]
            )

        if not PurchaseSaleOrder.objects.filter(
            id=purchase_sale_order.id, company=company
        ).exists():
            raise serializers.ValidationError(
                [
                    {
                        "purchase_sale_order": "A ordem de compra/venda deve pertencer à empresa fornecedora."
                    }
                ]
            )

        return attrs


class TripListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    transport_contract = serializers.CharField(
        source="transport_contract.id", read_only=True
    )
    driver = serializers.CharField(source="driver.id", read_only=True)
    vehicle = serializers.CharField(source="composition.id", read_only=True)
    quantity = serializers.FloatField(read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class TripCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = [
            "id",
            "transport_contract",
            "vehicle",
            "quantity",
            "date",
            "order_number",
        ]
        read_only_fields = ["id"]


class TripDetailSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    transport_contract = serializers.UUIDField(
        source="transport_contract.id", read_only=True
    )
    driver = serializers.UUIDField(source="driver.id", read_only=True)
    vehicle = serializers.CharField(source="vehicle.id", read_only=True)
    quantity = serializers.FloatField(read_only=True)
    date = serializers.DateField(read_only=True)
    order_number = serializers.CharField(read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
