from enum import StrEnum, unique


@unique
class SectorType(StrEnum):
    ROTATIVE = "ROTATIVE"
    CONTRACT = "CONTRACT"
