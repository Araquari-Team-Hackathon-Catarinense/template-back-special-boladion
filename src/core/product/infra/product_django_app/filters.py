from django.db.models import Q
from django_filters.rest_framework import CharFilter, FilterSet

from core.product.infra.product_django_app.models import Product


class ProductFilter(FilterSet):
    search = CharFilter(field_name="search", method="filter_search")

    def filter_search(self, queryset, name, value):
        try:
            return queryset.filter(
                Q(description__icontains=value) | Q(internal_code__icontains=value)
            )
        except Exception:
            return queryset

    class Meta:
        model = Product
        fields = ["search"]
