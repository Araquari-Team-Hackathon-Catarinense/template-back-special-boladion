import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from dotenv import load_dotenv
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.user.domain.actions import forget_password, reset_password, validate_token
from django_project.settings import API_VERSION

from .router import router

load_dotenv()
MODE = os.getenv("MODE")

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"api/{API_VERSION}/", include(router.urls)),
    path(f"api/{API_VERSION}/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        f"api/{API_VERSION}/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        f"api/{API_VERSION}/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path(
        f"api/{API_VERSION}/user/forget_passwords/",
        forget_password,
        name="user-forget_password",
    ),
    path(
        f"api/{API_VERSION}/user/reset_passwords/",
        reset_password,
        name="user-reset_password",
    ),
    path(
        f"api/{API_VERSION}/user/validate_tokens/",
        validate_token,
        name="user-validate_token",
    ),
    path(
        f"api/{API_VERSION}/user/token/",
        TokenObtainPairView.as_view(),
        name="user-token_obtain_pair",
    ),
    path(
        f"api/{API_VERSION}/user/token/refresh/",
        TokenRefreshView.as_view(),
        name="user-token_refresh",
    ),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if MODE == "staging":
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
