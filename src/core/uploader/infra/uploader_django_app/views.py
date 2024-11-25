from drf_spectacular.utils import extend_schema
from rest_framework import mixins, parsers, viewsets

from core.uploader.infra.uploader_django_app.models import Document
from core.uploader.infra.uploader_django_app.serializers import DocumentUploadSerializer


class CreateViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
    mixins.DestroyModelMixin,
):
    pass


@extend_schema(tags=["Core"])
class DocumentUploadViewSet(CreateViewSet):
    queryset = Document.objects.all()  #  pylint: disable=no-member
    serializer_class = DocumentUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
