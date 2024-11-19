from rest_framework import serializers

from core.uploader.domain.files import (
    CONTENT_TYPE_DOCUMENTS,
    CONTENT_TYPE_IMAGES,
    CONTENT_TYPE_PDF,
    get_content_type,
)
from core.uploader.infra.uploader_django_app.models import Document
from django_project.settings import BASE_URL


class DocumentUploadSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        url = BASE_URL + obj.file.url
        return url

    class Meta:
        model = Document
        fields = [
            "attachment_key",
            "file",
            "description",
            "uploaded_on",
            "type",
            "url",
            "id",
        ]
        read_only_fields = ["attachment_key", "uploaded_on", "url", "id"]
        extra_kwargs = {
            "file": {"write_only": True},
            "type": {"allow_null": True},
        }

    def validate(self, attrs):
        content_type = get_content_type(attrs["file"])
        if attrs.get("type") is not None:
            return attrs
        elif content_type in CONTENT_TYPE_IMAGES:
            attrs["type"] = "IMG"
        elif content_type in CONTENT_TYPE_PDF:
            attrs["type"] = "PDF"
        return attrs

    def validate_file(self, value):
        valid_content_types = CONTENT_TYPE_DOCUMENTS
        if get_content_type(value) not in valid_content_types:
            raise serializers.ValidationError(
                [{"file": "Arquivo inválido ou corrompido."}]
            )
        return value


class DocumentSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        url = BASE_URL + obj.file.url
        return url

    class Meta:
        model = Document
        fields = ["url", "description", "uploaded_on", "attachment_key", "id"]
        read_only_fields = ["url", "attachment_key", "uploaded_on", "id"]

    def create(self, validated_data):
        raise NotImplementedError(
            "Use DocumentUploadSerializer to create document files."
        )
