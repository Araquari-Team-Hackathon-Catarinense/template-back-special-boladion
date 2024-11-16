from enum import StrEnum, unique


@unique
class PersonType(StrEnum):
    PJ = "PJ"
    PF = "PF"

@unique
class ContractType(StrEnum):
    FORNECEDOR= "FORNECEDOR"
    CLIENTE ="CLIENTE"
    TRANSPORTADORA ="TRANSPORTADORA"
    ARMAZEM = "ARMAZEM"
    TERMINAL = "TERMINAL"
