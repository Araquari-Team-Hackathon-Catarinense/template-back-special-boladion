from rest_framework import serializers

from .models import Company


class CompanyListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)
    trade_name = serializers.CharField(read_only=True)
    person_type = serializers.CharField(read_only=True)
    document_member = serializers.CharField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
