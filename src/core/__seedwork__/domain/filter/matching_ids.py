from unidecode import unidecode


def get_matching_ids(queryset, field, normalized_value) -> list:
    """
    Retorna os IDs dos objetos no queryset onde o campo especificado
    contém o valor normalizado (ignorando acentos e diferenças de caixa).
    """
    matching_ids = []
    for item in queryset:
        field_value = getattr(item, field)
        if field_value is not None:
            if not isinstance(field_value, str):
                field_value = str(field_value)
            if normalized_value in unidecode(field_value).lower():
                matching_ids.append(item.id)
    return matching_ids
