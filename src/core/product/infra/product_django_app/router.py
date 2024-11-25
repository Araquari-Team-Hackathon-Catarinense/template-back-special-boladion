from rest_framework.routers import DefaultRouter

from core.product.infra.product_django_app.views import ProductViewSet

router = DefaultRouter()

router.register("product/products", ProductViewSet, basename="product-products")
