from enum import StrEnum, unique


@unique
class DocumentType(StrEnum):
    PDF = "PDF"
    IMG = "IMG"
    AVATAR = "AVATAR"
