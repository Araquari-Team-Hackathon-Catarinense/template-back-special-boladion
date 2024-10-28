from rest_framework import serializers

from core.company.domain.value_objects import ContractType
from core.company.infra.company_django_app.models import Contract
from core.order.infra.order_django_app.models import (
    MeasurementUnit,
    Packing,
    PurchaseSaleOrder,
)


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


class PurchaseSaleOrderListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    company = serializers.CharField(source="company.name", read_only=True)
    client = serializers.CharField(source="company.name", read_only=True)
    operation_terminal = serializers.CharField(source="company.name", read_only=True)
    product = serializers.CharField(source="product.description", read_only=True)
    measurement_unit = serializers.CharField(
        source="measurement_unit.description", read_only=True
    )
    packing = serializers.UUIDField(read_only=True)
    quantity = serializers.FloatField(read_only=True)
    balance = serializers.FloatField(read_only=True)
    operation_type = serializers.CharField(read_only=True)


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
            "balance",
            "operation_terminal",
            "operation_type",
        ]
        read_only_fields = ["id"]

    def validate(self, data) -> dict:
        company = data.get("company")
        client = data.get("client")
        operation_terminal = data.get("operation_terminal")

        print(company, client, operation_terminal)

        if not Contract.objects.filter(
            source_company=company, target_company=client, contract_type="CLIENTE"
        ).exists():
            print(
                Contract.objects.filter(
                    source_company=client,
                    target_company=company,
                    contract_type=ContractType.CLIENTE,
                )
            )
            raise serializers.ValidationError(
                "O cliente deve ser uma empresa com um contrato do tipo CLIENTE com a empresa fornecedora."
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
            or operation_terminal in {company.id, client.id}
        ):
            raise serializers.ValidationError(
                "O terminal de operação deve ser uma empresa com um contrato do tipo TERMINAL "
                "com a empresa fornecedora ou cliente, ou ser a própria empresa fornecedora ou cliente."
            )

        return data
