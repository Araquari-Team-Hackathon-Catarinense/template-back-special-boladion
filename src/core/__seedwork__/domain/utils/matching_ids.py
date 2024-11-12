from unidecode import unidecode


def get_matching_ids(queryset, field, normalized_value):
    """
    Retorna os IDs dos objetos no queryset onde o campo especificado
    contém o valor normalizado (ignorando acentos e diferenças de caixa).
    """
    return [
        item.id
        for item in queryset
        if getattr(item, field) is not None
        and normalized_value in unidecode(getattr(item, field)).lower()
    ]
