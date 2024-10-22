import uuid
from django.db import models
from django.utils import timezone
from safedelete.models import SafeDeleteModel
# from simple_history.models import HistoricalRecords


class BaseModel(SafeDeleteModel):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
        get_latest_by = "created_at"


# class BaseModelWithHistory(BaseModel):
#     history = HistoricalRecords(inherit=True)

#     class Meta:
#         abstract = True
#         ordering = ["-created_at"]
#         get_latest_by = "created_at"
