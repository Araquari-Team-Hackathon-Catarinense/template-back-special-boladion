from unidecode import unidecode


class Normalizer:
    @staticmethod
    def normalize_value(value):
        """
        Remove acentos e converte o valor para minúsculas.
        Para valores numéricos, converte o valor para string.
        """
        if isinstance(value, (int, float)):
            normalized_value = str(value)
        else:
            normalized_value = unidecode(str(value)).lower()
        return normalized_value
