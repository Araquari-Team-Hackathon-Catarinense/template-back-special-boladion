from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.uploader.infra.uploader_django_app.serializers import DocumentUploadSerializer

from .models import Driver, User
from .serializers import (
    DriverSerializerCreate,
    DriverSerializerList,
    UserCreateSerializer,
    UserDetailSerializer,
    UserListSerializer,
)


@extend_schema(tags=["user"])
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    authentication_classes = []

    def get_serializer_class(self):
        if self.action == "list":
            return UserListSerializer
        elif self.action == "retrieve":
            return UserDetailSerializer
        return UserCreateSerializer

    @action(detail=True, methods=["post"], url_path="upload-avatar")
    def upload_avatar(self, request, pk=None):
        data = request.data.copy()
        data["file"] = request.FILES.get("file")
        serializer = DocumentUploadSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user: User = self.get_object()
        if user.avatar:
            user.avatar.delete()
        user.avatar = serializer.instance
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DriverViewSet(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializerList
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "create":
            return DriverSerializerCreate
        if self.action == "patch":
            return DriverSerializerCreate
        return DriverSerializerList
