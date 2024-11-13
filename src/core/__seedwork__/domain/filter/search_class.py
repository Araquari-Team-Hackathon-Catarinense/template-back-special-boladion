from django.db import models
from django.db.models import Q

from .matching_ids import get_matching_ids


class SearchClass:
    def __init__(self, queryset, field, normalized_value):
        self.queryset = queryset
        self.field = field
        self.normalized_value = normalized_value

    def apply_search(self, matching_ids):
        """
        Aplica o filtro específico do tipo de campo, atualizando os matching_ids se necessário.
        """
        field_name = self.field.name
        if isinstance(self.field, (models.CharField, models.TextField)):
            return self._search_char_field(matching_ids)
        elif (
            isinstance(self.field, (models.IntegerField, models.FloatField))
            and self.normalized_value.isdigit()
        ):
            return Q(**{f"{field_name}": self.normalized_value})
        elif isinstance(self.field, models.UUIDField):
            return Q(**{f"{field_name}__icontains": self.normalized_value})
        elif isinstance(self.field, models.ManyToManyField):
            return self._search_many_to_many_field(matching_ids)
        elif isinstance(self.field, models.ForeignKey):
            return self._search_foreign_key_field(matching_ids)
        return Q()

    def _search_char_field(self, matching_ids):
        """
        Filtro para campos de string.
        """
        matching_ids.update(
            get_matching_ids(self.queryset, self.field.name, self.normalized_value)
        )
        return Q(**{f"{self.field.name}__icontains": self.normalized_value})

    def _search_many_to_many_field(self, matching_ids):
        """
        Filtro para campos ManyToMany.
        """
        matching_ids.update(
            get_matching_ids(
                self.queryset, f"{self.field.name}__name", self.normalized_value
            )
        )
        return Q(**{f"{self.field.name}_name__icontains": self.normalized_value})

    def _search_foreign_key_field(self, matching_ids):
        """
        Filtro para campos ForeignKey, verificando os campos relacionados.
        """
        field_name = self.field.name
        related_model = self.field.related_model
        query = Q()

        matching_ids.update(
            get_matching_ids(self.queryset, f"{field_name}_id", self.normalized_value)
        )

        related_model_fields = {
            field.name
            for field in related_model._meta.get_fields()  # pylint: disable=protected-access
        }

        if "name" in related_model_fields:

            query |= Q(**{f"{field_name}__name__icontains": self.normalized_value})

        try:
            if "description" in related_model_fields:

                query |= Q(
                    **{f"{field_name}__description__icontains": self.normalized_value}
                )
        except AttributeError:

            query |= Q(**{f"{field_name}_id__icontains": self.normalized_value})

        try:
            if "document_number" in related_model_fields:
                query |= Q(
                    **{
                        f"{field_name}__document_number__icontains": self.normalized_value
                    }
                )
        except AttributeError:
            query |= Q(**{f"{field_name}_id__icontains": self.normalized_value})

        return query

    def _search_related_field(self, matching_ids, field_name, related_field):
        """
        Função auxiliar para aplicar filtro em um campo específico de um modelo relacionado.
        """
        matching_ids.update(
            get_matching_ids(
                self.queryset, f"{field_name}__{related_field}", self.normalized_value
            )
        )
        return Q(**{f"{field_name}__{related_field}__icontains": self.normalized_value})
