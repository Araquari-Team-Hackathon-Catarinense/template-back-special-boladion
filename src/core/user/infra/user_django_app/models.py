import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.uploader.infra.uploader_django_app.admin import Document

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True, editable=True, default=uuid.uuid4)
    email = models.EmailField(_("e-mail address"), unique=True)
    name = models.CharField(max_length=255, null=True)
    cpf = models.CharField(max_length=14, null=True, unique=True)
    address = models.JSONField(null=True, blank=True)
    password_reset_token = models.CharField(
        _("Password Reset Token"), max_length=255, blank=True, null=True
    )
    password_reset_token_created = models.DateTimeField(
        _("Password Reset Token Created"), blank=True, null=True
    )
    avatar = models.ForeignKey(
        Document,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email + " - " + (self.name or "No Name")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]
