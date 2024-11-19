import datetime

from pycpfcnpj import cpf
from rest_framework import serializers
from rest_framework_simplejwt.serializers import AuthUser, TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token

from core.uploader.infra.uploader_django_app.admin import Document
from django_project.settings import BASE_URL

from .models import Driver, User


class UserDetailSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    email = serializers.EmailField(read_only=True)
    name = serializers.CharField(read_only=True)
    cpf = serializers.CharField(read_only=True)
    address = serializers.JSONField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    avatar = serializers.SerializerMethodField(read_only=True)

    def get_avatar(self, obj):
        if isinstance(obj, dict):
            if obj.get("avatar") is None:
                return None
        if obj.avatar is None:
            return None
        url = BASE_URL + obj.avatar.url
        return url

    def create(self, validated_data):
        return NotImplementedError

    def update(self, instance, validated_data):
        return NotImplementedError


class ParcialUserSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField()
    cpf = serializers.CharField()


class UserListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    email = serializers.EmailField()
    name = serializers.CharField()
    cpf = serializers.CharField()
    address = serializers.JSONField()
    avatar = serializers.SerializerMethodField()

    def get_avatar(self, obj):
        if isinstance(obj, dict):
            if obj.get("avatar") is None:
                return None
        if not obj.avatar:
            return None
        url = BASE_URL + obj.avatar.url
        return url

    def create(self, validated_data):
        return NotImplementedError

    def update(self, instance, validated_data):
        return NotImplementedError


class UserCreateSerializer(serializers.ModelSerializer):
    avatar_attachment_key = serializers.SlugRelatedField(
        source="avatar",
        queryset=Document.objects.all(),
        slug_field="attachment_key",
        required=False,
        allow_null=True,
        write_only=True,
    )
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
        model = User
        fields = [
            "id",
            "email",
            "name",
            "password",
            "cpf",
            "address",
            "avatar_attachment_key",
            "avatar",
        ]
        read_only_fields = ["id", "avatar"]

    def validate_cpf(self, value: str) -> str:
        if not cpf.validate(value):
            raise serializers.ValidationError([{"cpf": "CPF inválido."}])
        return value

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        validated_data["password"] = user.password
        return super().create(validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def create(self, validated_data):
        return NotImplementedError

    def update(self, instance, validated_data):
        return NotImplementedError

    @classmethod
    def get_token(cls, user: AuthUser) -> Token:
        token: Token = super().get_token(user)
        user_id: str = token["user_id"]
        user: User = User.objects.get(id=user_id)

        user_companies = []
        for employee in user.employees.all():
            company = {
                "id": str(employee.company.id),
                "name": employee.company.name,
                "avatar": (
                    BASE_URL + employee.company.avatar.url
                    if employee.company.avatar
                    else None
                ),
            }
            user_companies.append(company)

        user_data: dict = {
            "name": user.name,
            "email": user.email,
            "avatar": BASE_URL + user.avatar.url if user.avatar else None,
            "companies": user_companies,
        }
        token["user"] = user_data

        return token

    # def validate(self, attrs):
    #     email: str = attrs.get("email")
    #     password: str = attrs.get("password")

    #     if email and password:
    #         user = authenticate(
    #             request=self.context.get("request"), email=email, password=password
    #         )
    #         user = User.objects.get(email=email)
    #         user.is_confirmed = True
    #         user.save()
    #         if not user:
    #             raise serializers.ValidationError("Invalid email or password")
    #     else:
    #         raise serializers.ValidationError('Must include "email" and "password"')

    #     return super().validate(attrs)


class DriverListSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    license_number = serializers.CharField(read_only=True)
    license_category = serializers.CharField(read_only=True)
    valid_until_license = serializers.DateField(read_only=True)
    phone = serializers.CharField(read_only=True)
    user = ParcialUserSerializer(read_only=True)

    def create(self, validated_data):
        return NotImplementedError

    def update(self, instance, validated_data):
        return NotImplementedError


class DriverCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            "license_number",
            "license_category",
            "valid_until_license",
            "phone",
            "user",
        ]
        read_only_fields = ["id"]

    def validate(self, attrs):
        valid_until_license = attrs.get("valid_until_license")
        date = datetime.date.today()
        if valid_until_license < date:
            raise serializers.ValidationError(
                [{"valid_until_license": "Data de validade expirada."}]
            )
        return attrs
