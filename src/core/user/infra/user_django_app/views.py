from django.forms import model_to_dict
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.uploader.infra.uploader_django_app.serializers import DocumentUploadSerializer
from core.user.infra.user_django_app.filters import UserFilter

from .models import Driver, User
from .serializers import (
    DriverCreateSerializer,
    DriverListSerializer,
    UserCreateSerializer,
    UserDetailSerializer,
    UserListSerializer,
)


@extend_schema(tags=["User"])
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]
    authentication_classes = []
    filterset_class = UserFilter

    def get_serializer_class(self):
        if self.action == "list":
            return UserListSerializer
        elif self.action == "retrieve":
            return UserDetailSerializer
        return UserCreateSerializer

    @action(
        detail=True,
        methods=["post"],
        url_path="upload-avatar",
    )
    def upload_avatar(self, request, pk=None, *args, **kwargs):
        try:
            user: User = self.get_object()
            data = request.data.copy()
            if (
                "description" not in data
                or data["description"] is None
                or data["description"] == ""
            ):
                data["description"] = f"Avatar do usuario {user.name}"
            data["file"] = request.FILES.get("file")
            serializer = DocumentUploadSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            if user.avatar:
                user.avatar.delete()
            user.avatar = serializer.instance
            user.save()
            user_detail_serializer = UserDetailSerializer(user)
            return Response(user_detail_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=["User"])
class DriverViewSet(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverListSerializer
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DriverListSerializer
        return DriverCreateSerializer
