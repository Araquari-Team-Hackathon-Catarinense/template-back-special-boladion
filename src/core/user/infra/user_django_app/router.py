from rest_framework.routers import DefaultRouter

from core.user.infra.user_django_app import views  # pylint: disable=global-statement

app_name = "core.user.infra.user_django_app"

router = DefaultRouter()

router.register("user/drivers", views.DriverViewSet, basename="user-driver")
router.register("user/users", views.UserViewSet, basename="user-users")
