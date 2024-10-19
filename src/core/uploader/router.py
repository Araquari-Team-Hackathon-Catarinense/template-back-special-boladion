from rest_framework.routers import DefaultRouter

from core.uploader import views

app_name = "uploader"

router = DefaultRouter()
router.register("documents", views.DocumentUploadViewSet)
