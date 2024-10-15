from enum import StrEnum, unique


@unique
class PersonType(StrEnum):
    PJ = "PJ"
    PF = "PF"
