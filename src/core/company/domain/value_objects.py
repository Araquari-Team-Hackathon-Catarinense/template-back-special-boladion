from enum import StrEnum, unique


@unique
class PersonType(StrEnum):
    PJ = "PJ"
    PF = "PF"

@unique
class ContractType(StrEnum):
    FORNECEDOR= "Fornecedor"
    CLIENTE ="Cliente"
    TRANSPORTADORA ="Transportadora"
    ARMAZEM = "Armazem"
    TERMINAL = "Terminal"
