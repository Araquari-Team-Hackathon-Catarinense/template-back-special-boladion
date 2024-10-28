from enum import StrEnum, unique


@unique
class OperationType(StrEnum):
    CARGA = "Carga"
    DESCARGA = "Descarga"
