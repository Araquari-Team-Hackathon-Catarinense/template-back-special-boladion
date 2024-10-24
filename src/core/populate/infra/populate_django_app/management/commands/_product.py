from core.populate.infra.resources.data_product import generate_products
from core.product.infra.product_django_app.models import Product


def populate_products() -> None:
    if Product.objects.exists():
        return

    products_to_create: list[Product] = [
        Product(**data) for data in generate_products()
    ]
    Product.objects.bulk_create(products_to_create)
