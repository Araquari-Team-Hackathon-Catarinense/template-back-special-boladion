from django.db import models
from django.db.models import Q
from django_filters import rest_framework as filters
from unidecode import unidecode

from core.__seedwork__.domain.utils.matching_ids import get_matching_ids


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
        Executa uma busca global insensível a acentos e caixa, utilizando `get_matching_ids`
        para verificar os dados normalizados.
        """
        normalized_value = unidecode(value).lower()
        query = Q()
        matching_ids = set()

        for field in queryset.model._meta.fields:
            field_name = field.name
            try:
                if isinstance(field, (models.CharField, models.TextField)):
                    query |= Q(**{f"{field_name}__icontains": normalized_value})
                    matching_ids.update(
                        get_matching_ids(queryset, field_name, normalized_value)
                    )
                elif (
                    isinstance(field, (models.IntegerField, models.FloatField))
                    and value.isdigit()
                ):
                    query |= Q(**{f"{field_name}": value})
                elif isinstance(field, models.UUIDField):
                    query |= Q(**{f"{field_name}__icontains": normalized_value})
                elif isinstance(field, models.ManyToManyField):
                    query |= Q(**{f"{field_name}__name__icontains": normalized_value})
                    matching_ids.update(
                        get_matching_ids(
                            queryset, f"{field_name}__name", normalized_value
                        )
                    )
                elif isinstance(field, models.ForeignKey):
                    query |= Q(**{f"{field_name}__id__icontains": normalized_value})

                    related_model = field.related_model
                    if hasattr(related_model, "name"):
                        related_field_name = f"{field_name}__name"
                        query |= Q(
                            **{f"{related_field_name}__icontains": normalized_value}
                        )
                        matching_ids.update(
                            get_matching_ids(
                                queryset, related_field_name, normalized_value
                            )
                        )

                    if hasattr(related_model, "description"):
                        related_field_description = f"{field_name}__description"
                        query |= Q(
                            **{
                                f"{related_field_description}__icontains": normalized_value
                            }
                        )

                    if hasattr(related_model, "document_number"):
                        related_field_document_number = f"{field_name}__document_number"
                        query |= Q(
                            **{
                                f"{related_field_document_number}__icontains": normalized_value
                            }
                        )
            except ValueError as exc:
                raise ValueError(f"Invalid field {field_name}") from exc

        return queryset.filter(query | Q(id__in=matching_ids))
