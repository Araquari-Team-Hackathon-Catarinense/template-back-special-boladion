import os
from dotenv import load_dotenv

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.user.domain.actions import forget_password, reset_password, validate_token
from core.vehicle.infra.vehicle_django_app.views import VehicleCompositionApiView

from .router import router

load_dotenv()
MODE = os.getenv("MODE")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/v1/user/forget_passwords/", forget_password, name="user-forget_password"),
    path("api/v1/user/reset_passwords/", reset_password, name="user-reset_password"),
    path("api/v1/user/validate_tokens/", validate_token, name="user-validate_token"),
    path(
        "api/v1/user/token/",
        TokenObtainPairView.as_view(),
        name="user-token_obtain_pair",
    ),
    path(
        "api/v1/user/token/refresh/",
        TokenRefreshView.as_view(),
        name="user-token_refresh",
    ),
    path(
        "api/v1/vehicle/get-vehicle-composition/",
        VehicleCompositionApiView.as_view(),
        name="vehicle-get-vehicle-composition",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




if MODE == "staging":
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
