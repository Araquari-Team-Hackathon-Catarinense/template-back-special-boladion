from django.db import models

from core.__seedwork__.infra.django_app.models import BaseModel


# Create your models here.
class Body(BaseModel):
    description = models.CharField(max_length=45)
