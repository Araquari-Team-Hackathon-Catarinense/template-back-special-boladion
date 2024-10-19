from rest_framework import mixins, parsers, viewsets

from core.uploader.models import Document
from core.uploader.serializers import DocumentUploadSerializer


class CreateViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    pass


class DocumentUploadViewSet(CreateViewSet):
    queryset = Document.objects.all()  #  pylint: disable=no-member
    serializer_class = DocumentUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
