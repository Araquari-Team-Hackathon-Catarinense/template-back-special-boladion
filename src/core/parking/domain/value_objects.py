from enum import StrEnum, unique


@unique
class SectorType(StrEnum):
    is_free = "is_free"
    is_contract = "is_contract"
