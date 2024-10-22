from rest_framework.routers import DefaultRouter

from .views import ImageProfilePicViewSet

router = DefaultRouter()

router.register(r"profile_pics", ImageProfilePicViewSet, basename="profilePic")
