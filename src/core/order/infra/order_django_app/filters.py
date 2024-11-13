from django_filters.rest_framework import CharFilter

from core.__seedwork__.infra.django_app.basefilter import BaseFilter
from core.order.infra.order_django_app.models import (
    MeasurementUnit,
    Packing,
    PurchaseSaleOrder,
)


class MeasurementUnitFilter(BaseFilter):
    search = CharFilter(
        field_name="search", method="global_search_for_strings_and_numbers"
    )

    class Meta:
        model = MeasurementUnit
        fields = ["search"]


class PackingFilter(BaseFilter):
    search = CharFilter(
        field_name="search", method="global_search_for_strings_and_numbers"
    )

    class Meta:
        model = Packing
        fields = ["search"]


class PurchaseSaleOrderFilter(BaseFilter):
    search = CharFilter(
        field_name="search", method="global_search_for_strings_and_numbers"
    )

    class Meta:
        model = PurchaseSaleOrder
        fields = ["search"]
