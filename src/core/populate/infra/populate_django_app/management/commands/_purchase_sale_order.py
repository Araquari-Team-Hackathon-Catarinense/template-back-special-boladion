from core.order.infra.order_django_app.models import PurchaseSaleOrder
from core.populate.infra.resources.data_purchase_sale_order import (
    generate_purchase_sale_orders,
)


def populate_purchase_sale_orders() -> None:
    if PurchaseSaleOrder.objects.exists():
        return

    purchase_sale_orders_to_create = [
        PurchaseSaleOrder(**data) for data in generate_purchase_sale_orders()
    ]
    PurchaseSaleOrder.objects.bulk_create(purchase_sale_orders_to_create)
