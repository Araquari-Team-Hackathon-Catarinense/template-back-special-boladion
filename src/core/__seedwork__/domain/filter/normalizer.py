from unidecode import unidecode


class Normalizer:
    @staticmethod
    def normalize_value(value):
        """
        Remove acentos e converte o valor para minúsculas.
        Para valores numéricos, converte o valor para string.
        """
        if isinstance(value, (int, float)):
            # Converte o número para string antes de normalizar
            normalized_value = str(value)
        else:
            # Converte para string e aplica unidecode e lower
            normalized_value = unidecode(str(value)).lower()

        print(
            f"Valor original: {value} | Valor normalizado: {normalized_value}"
        )  # Log para depuração
        return normalized_value
