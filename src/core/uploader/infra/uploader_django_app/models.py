import mimetypes
import uuid

from django.db import models

from core.__seedwork__.infra.django_app.models import BaseModel
from core.uploader.domain.files import get_content_type
from core.uploader.domain.value_objects import DocumentType


def document_file_path(document, _) -> str:
    if document.type == "PDF":
        content_type = get_content_type(document.file)
        extension: str = mimetypes.guess_extension(content_type)

    elif document.type == "IMG":
        content_type = get_content_type(document.file)
        extension: str = mimetypes.guess_extension(content_type)
        if extension == ".jpe":
            extension = ".jpg"
    elif document.type == "AVATAR":
        extension = ".png"
    return f"documents/{document.public_id}{extension or ''}"


class Document(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        (document_type.name, document_type.value) for document_type in DocumentType
    ]

    attachment_key = models.UUIDField(
        max_length=255,
        default=uuid.uuid4,
        unique=True,
        help_text=(
            "Used to attach the document to another object. "
            "Cannot be used to retrieve the document file."
        ),
    )
    public_id = models.UUIDField(
        max_length=255,
        default=uuid.uuid4,
        unique=True,
        help_text=(
            "Used to retrieve the document file itself. "
            "Should not be readable until the document is attached to another object."
        ),
    )
    file = models.FileField(upload_to=document_file_path)
    description = models.CharField(max_length=255, blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=6, choices=DOCUMENT_TYPE_CHOICES, default="PDF")

    def __str__(self) -> str:
        return f"{self.description} - {self.file.name}"

    @property
    def url(self) -> str:
        return self.file.url  # pylint: disable=no-member
