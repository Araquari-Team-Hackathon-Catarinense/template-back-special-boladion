from django_filters.rest_framework.filters import CharFilter

from core.__seedwork__.infra.django_app.basefilter import BaseFilter
from core.user.infra.user_django_app.models import User


class UserFilter(BaseFilter):
    name = CharFilter(method="global_filter_for_strings")
    cpf = CharFilter(method="global_filter_for_strings")

    search = CharFilter(method="global_search_for_strings_and_numbers")

    class Meta:
        model = User
        fields = ["name", "cpf", "search"]
