from re import search

from django.db.models import Q
from django_filters.rest_framework import CharFilter, FilterSet

from core.order.infra.order_django_app.models import (
    MeasurementUnit,
    Packing,
    PurchaseSaleOrder,
)


class MeasurementUnitFilter(FilterSet):
    search = CharFilter(field_name="search", method="filter_search")

    def filter_search(self, queryset, name, value):
        try:
            return queryset.filter(description__icontains=value)
        except Exception:
            return queryset

    class Meta:
        model = MeasurementUnit
        fields = ["search"]


class PackingFilter(FilterSet):
    search = CharFilter(field_name="search", method="filter_search")

    def filter_search(self, queryset, name, value):
        try:
            return queryset.filter(description__icontains=value)
        except Exception:
            return queryset

    class Meta:
        model = Packing
        fields = ["search"]


class PurchaseSaleOrderFilter(FilterSet):
    search = CharFilter(field_name="search", method="filter_search")

    def filter_search(self, queryset, name, value):
        try:
            return queryset.filter(
                Q(client__name__icontains=value)
                | Q(client__document_number__icontains=value)
                | Q(operation_terminal__name__icontains=value)
                | Q(operation_terminal__document_number__icontains=value)
                | Q(product__description__icontains=value)
                | Q(product__internal_code__icontains=value)
            )
        except Exception:
            return queryset

    class Meta:
        model = PurchaseSaleOrder
        fields = ["search"]
