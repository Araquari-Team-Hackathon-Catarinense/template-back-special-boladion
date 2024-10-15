from os import read
from pycpfcnpj import cpf, cnpj, cpfcnpj
from rest_framework import serializers

from .models import Company


class CompanyListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    trade_name = serializers.CharField(read_only=True)
    person_type = serializers.CharField(read_only=True)
    document_member = serializers.CharField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "trade_name",
            "person_type",
            "document_number",
            "is_active",
        ]
        read_only_fields = ["id"]

    def validate_document_number(self, value: str) -> str:
        if self.initial_data["person_type"] == "PJ":
            if not cnpj.validate(value):
                raise serializers.ValidationError("Invalid CNPJ.")
        elif self.initial_data["person_type"] == "PF":
            if not cpf.validate(value):
                raise serializers.ValidationError("Invalid CPF.")
        elif not cpfcnpj.validate(value):
            raise serializers.ValidationError("Invalid document number.")
        return value
