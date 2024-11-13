from django.db.models import Q
from django_filters import rest_framework as filters
from unidecode import unidecode

from core.__seedwork__.domain.filter.matching_ids import get_matching_ids
from core.__seedwork__.domain.filter.normalizer import Normalizer
from core.__seedwork__.domain.filter.search_class import SearchClass


class BaseFilter(filters.FilterSet):
    """
    Filtro base para os filtros de pesquisa.
    """

    def global_filter_for_strings(self, queryset, field, value):
        """
        Filtra o queryset de acordo com o valor passado, tirando os acentos e convertendo para minúsculo.
        """
        try:
            if value is None:
                return queryset
            normalized_value = unidecode(value).lower()
            matching_ids = get_matching_ids(queryset, field, normalized_value)
            return queryset.filter(id__in=matching_ids)
        except ValueError as exc:
            raise ValueError(f"Invalid field {field}") from exc

    def global_search_for_strings_and_numbers(
        self, queryset, name, value
    ):  # pylint: disable=unused-argument
        """
        Executa uma busca global insensível a acentos e caixa em campos relevantes.
        """
        normalized_value = Normalizer.normalize_value(value)
        query = Q()
        matching_ids = set()

        for field in queryset.model._meta.fields:  # pylint: disable=protected-access
            search_class = SearchClass(queryset, field, normalized_value)
            query |= search_class.apply_search(matching_ids)

        return queryset.filter(query | Q(id__in=matching_ids))
