from django.db.models import Q
from django_filters.rest_framework import CharFilter, FilterSet, NumberFilter

from core.company.infra.company_django_app.models import Company


class CompanyFilter(FilterSet):
    search = CharFilter(field_name="search", method="filter_search")

    def filter_search(self, queryset, name, value):
        try:
            return queryset.filter(
                Q(name__icontains=value)
                | Q(trade_name__icontains=value)
                | Q(document_number__icontains=value)
            )
        except Exception:
            return queryset

    class Meta:
        model = Company
        fields = ["search"]
