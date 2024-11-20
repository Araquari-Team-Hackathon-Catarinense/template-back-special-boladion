from dill import source
from pycpfcnpj import cnpj, cpf, cpfcnpj
from rest_framework import serializers

from core.uploader.infra.uploader_django_app.models import Document
from core.uploader.infra.uploader_django_app.serializers import DocumentSerializer
from django_project.settings import BASE_URL

from .models import Company, Contract, Employee


class CompanyListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    trade_name = serializers.CharField(read_only=True)
    person_type = serializers.CharField(read_only=True)
    document_number = serializers.CharField(read_only=True)
    address = serializers.JSONField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    avatar = serializers.SerializerMethodField(read_only=True)

    def get_avatar(self, obj):
        if isinstance(obj, dict):
            if obj.get("avatar") is None:
                return None
        if not obj.avatar:
            return None
        url = BASE_URL + obj.avatar.url
        return url


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
    documents = DocumentSerializer(
        read_only=True,
        many=True,
    )
    avatar = serializers.SerializerMethodField(read_only=True)

    def get_avatar(self, obj):
        if isinstance(obj, dict):
            if obj.get("avatar") is None:
                return None
        if not obj.avatar:
            return None
        url = BASE_URL + obj.avatar.url
        return url

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if rep["avatar"] is None:
            rep.pop("avatar")

        return rep


class CompanyCreateSerializer(serializers.ModelSerializer):
    avatar_attachment_key = serializers.SlugRelatedField(
        source="avatar",
        queryset=Document.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    documents_attachment_keys = serializers.SlugRelatedField(
        source="documents",
        queryset=Document.objects.all(),
        slug_field="attachment_key",
        required=False,
        many=True,
        write_only=True,
    )
    documents = DocumentSerializer(read_only=True, many=True)
    avatar = serializers.SerializerMethodField(read_only=True)

    def get_avatar(self, obj):
        if isinstance(obj, dict):
            if obj.get("avatar") is None:
                return None
        if obj.avatar is None:
            return None
        url = BASE_URL + obj.avatar.url
        return url

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
            "documents",
            "documents_attachment_keys",
            "avatar_attachment_key",
            "avatar",
        ]
        read_only_fields = ["id"]

    def validate_document_number(self, value: str) -> str:
        if self.initial_data["person_type"] == "PJ":
            if not cnpj.validate(value):
                raise serializers.ValidationError(
                    [{"document_number": "CNPJ inválido."}]
                )
        elif self.initial_data["person_type"] == "PF":
            if not cpf.validate(value):
                raise serializers.ValidationError(
                    [{"document_number": "CPF inválido."}]
                )
        elif not cpfcnpj.validate(value):
            raise serializers.ValidationError(
                [{"document_number": "CPF/CNPJ inválido."}]
            )
        return value


class EmployeeUserInfoSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)


class EmployeeListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    company = serializers.CharField(source="company.name", read_only=True)
    user = EmployeeUserInfoSerializer(read_only=True)
    is_active = serializers.BooleanField(read_only=True)


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id",
            "company",
            "user",
            "is_active",
        ]
        read_only_fields = ["id"]
        extra_kwargs = {"company": {"write_only": True}}


class ContractCompanyInfoSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    avatar = serializers.SerializerMethodField(read_only=True)

    def get_avatar(self, obj):
        if isinstance(obj, dict):
            if obj.get("avatar") is None:
                return None
        if obj.avatar is None:
            return None
        url = BASE_URL + obj.avatar.url
        return url


class ContractListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    source_company = ContractCompanyInfoSerializer(read_only=True)
    target_company = ContractCompanyInfoSerializer(read_only=True)
    contract_type = serializers.CharField(read_only=True)


class ContractCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            "id",
            "source_company",
            "target_company",
            "contract_type",
        ]
        read_only_fields = ["id"]
