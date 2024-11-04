from enum import StrEnum, unique


@unique
class VehicleType(StrEnum):
    TRACIONADORA = "Tracionadora"
    CARRETA = "Carreta"
    DOLLY = "Dolly"
    MOTO = "Moto"
    CARRO = "Carro"
    CAMIONETA = "Camioneta"
