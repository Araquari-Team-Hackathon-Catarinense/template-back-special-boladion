from django.contrib.auth import authenticate
from pycpfcnpj import cpf
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    name = serializers.CharField()
    cpf = serializers.CharField()
    address = serializers.JSONField()
    is_active = serializers.BooleanField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)


class UserListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    name = serializers.CharField()
    cpf = serializers.CharField()
    address = serializers.JSONField()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "name",
            "cpf",
            "address",
        ]
        read_only_fields = ["id"]

    def validate_cpf(self, value: str) -> str:
        if not cpf.validate(value):
            raise serializers.ValidationError("Invalid CPF.")
        return value


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"), email=email, password=password
            )
            user = User.objects.get(email=email)
            user.is_confirmed = True
            user.save()
            if not user:
                raise serializers.ValidationError("Invalid email or password")
        else:
            raise serializers.ValidationError('Must include "email" and "password"')

        return super().validate(attrs)
