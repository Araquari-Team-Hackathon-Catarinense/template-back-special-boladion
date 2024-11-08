import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.__seedwork__.infra.django_app.models import BaseModel
from core.uploader.infra.uploader_django_app.admin import Document
from core.user.domain.value_objects import DriveLicenseCategoryType

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


class Driver(BaseModel):
    LICENSE_CATEGORY_CHOICES = [
        (license_category.name, license_category.value)
        for license_category in DriveLicenseCategoryType
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=45, null=True, unique=True)
    license_category = models.CharField(
        max_length=2, null=True, blank=True, choices=LICENSE_CATEGORY_CHOICES
    )
    valid_until_license = models.DateField(null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
