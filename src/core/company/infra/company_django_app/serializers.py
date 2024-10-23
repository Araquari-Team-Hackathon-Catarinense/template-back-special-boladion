from pycpfcnpj import cnpj, cpf, cpfcnpj
from rest_framework import serializers

from core.uploader.models import Document
from core.uploader.serializers import DocumentSerializer

from .models import Company, Employee


class CompanyListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    trade_name = serializers.CharField(read_only=True)
    person_type = serializers.CharField(read_only=True)
    document_number = serializers.CharField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)


class CompanyDetailSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    trade_name = serializers.CharField(read_only=True)
    person_type = serializers.CharField(read_only=True)
    document_number = serializers.CharField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    address = serializers.JSONField(read_only=True)
    contacts = serializers.JSONField(read_only=True)
    system_admin = serializers.BooleanField(read_only=True)
    document = DocumentSerializer(read_only=True)


class CompanyCreateSerializer(serializers.ModelSerializer):
    document_attachment_key = serializers.SlugRelatedField(
        source="document",
        queryset=Document.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    document = DocumentSerializer(read_only=True, required=False)

    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "trade_name",
            "person_type",
            "document_number",
            "is_active",
            "address",
            "contacts",
            "system_admin",
            "document",
            "document_attachment_key",
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


class EmployeeListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    company_id = serializers.UUIDField(source="company_id.id", read_only=True)
    user_id = serializers.IntegerField(source="user_id.id", read_only=True)
    is_active = serializers.BooleanField(read_only=True)


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "company_id",
            "user_id",
            "is_active",
        ]
        read_only_fields = ["id"]
