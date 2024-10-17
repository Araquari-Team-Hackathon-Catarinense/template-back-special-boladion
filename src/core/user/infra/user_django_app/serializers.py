from django.contrib.auth import authenticate
from pycpfcnpj import cpf
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token

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

    def create(self, validated_data):
        return NotImplementedError

    def update(self, instance, validated_data):
        return NotImplementedError

    @classmethod
    def get_token(cls, user: User) -> Token:
        token: Token = super().get_token(user)
        user_id = token["user_id"]
        users: User = User.objects.filter(id=user_id)

        for user in users:
            user_data: dict = {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "cpf": user.cpf,
                "address": user.address,
            }
            token["user"] = user_data

        return token

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
