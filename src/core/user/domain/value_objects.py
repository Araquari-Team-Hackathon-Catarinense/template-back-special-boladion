from enum import StrEnum, unique


@unique
class DriveLicenseCategoryType(StrEnum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    AB = "AB"
    AC = "AC"
    AD = "AD"
    AE = "AE"
