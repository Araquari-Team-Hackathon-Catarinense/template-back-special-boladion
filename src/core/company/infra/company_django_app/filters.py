from django_filters.rest_framework import CharFilter

from core.__seedwork__.infra.django_app.basefilter import BaseFilter
from core.company.infra.company_django_app.models import Company, Contract

# class CompanyFilter(FilterSet):
#     search = CharFilter(field_name="search", method="filter_search")

#     def filter_search(self, queryset, name, value):
#         try:
#             return queryset.filter(
#                 Q(name__icontains=value)
#                 | Q(trade_name__icontains=value)
#                 | Q(document_number__icontains=value)
#             )
#         except Exception:
#             return queryset

#     class Meta:
#         model = Company
#         fields = ["search"]


class CompanyFilter(BaseFilter):
    search = CharFilter(
        field_name="search", method="global_search_for_strings_and_numbers"
    )

    class Meta:
        model = Company
        fields = ["search"]


class ContractFilter(BaseFilter):
    type = CharFilter(field_name="contract_type")
    search = CharFilter(
        field_name="search", method="global_search_for_strings_and_numbers"
    )

    class Meta:
        model = Contract
        fields = ["type", "search"]
