from rest_framework.routers import DefaultRouter

from core.uploader.infra.uploader_django_app import views

app_name = "uploader"

router = DefaultRouter()
router.register("uploader/documents", views.DocumentUploadViewSet)
