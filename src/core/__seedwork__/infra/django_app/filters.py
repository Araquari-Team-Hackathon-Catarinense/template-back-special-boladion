from django.db import models
from django.db.models import Q
from django_filters import rest_framework as filters
from unidecode import unidecode


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
            matching_ids = [
                item.id
                for item in queryset
                if getattr(item, field) is not None
                and normalized_value in unidecode(getattr(item, field)).lower()
            ]
            return queryset.filter(id__in=matching_ids)
        except ValueError as exc:
            raise ValueError(f"Invalid field {field}") from exc

    def global_search_for_strings_and_numbers(
        self,
        queryset,
        name,
        value,
    ):  # pylint: disable=unused-argument
        """
        Executa uma busca global em todos os campos relevantes do modelo no queryset.
        Se o campo for do tipo string, ele irá buscar por um valor que contenha o valor passado.
        Se o campo for do tipo inteiro, ele irá buscar por um valor exato.
        A função unidecode é utilizada para remover acentos e caracteres especiais.
        """
        normalized_value = unidecode(value).lower()
        query = Q()

        for field in queryset.model._meta.fields:  # pylint: disable=protected-access
            field_name = field.name
            try:
                if isinstance(field, (models.CharField, models.TextField)):
                    query |= Q(**{f"{field_name}__icontains": normalized_value})
                elif (
                    isinstance(field, (models.IntegerField, models.FloatField))
                    and value.isdigit()
                ):
                    query |= Q(**{f"{field_name}__icontains": value})
                elif isinstance(field, models.UUIDField):
                    query |= Q(**{f"{field_name}__icontains": normalized_value})
                # elif isinstance(field, models.BooleanField):
                #     query |= Q(**{f"{field_name}": value})
                elif isinstance(field, models.ManyToManyField):
                    query |= Q(**{f"{field_name}__name__icontains": normalized_value})
                elif isinstance(field, models.ForeignKey):
                    query |= Q(**{f"{field_name}__id__icontains": normalized_value})

                    related_model = field.related_model

                    if hasattr(related_model, "name"):
                        related_field_name = f"{field_name}__name"
                        query |= Q(
                            **{f"{related_field_name}__icontains": normalized_value}
                        )
                    if hasattr(related_model, "description"):
                        related_field_description = f"{field_name}__description"
                        query |= Q(
                            **{
                                f"{related_field_description}__icontains": normalized_value
                            }
                        )
            except (AttributeError, TypeError, ValueError) as e:
                print(f"Erro ao tentar acessar o campo {field_name}: {e}")

        return queryset.filter(query)
