from transporte import Transporte


class TransporteTerreste(Transporte):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: int, motor: str, rodas: str):
        Transporte.__init__(self, nome, altura, comprimento, carga, velocidade)
        self.__motor = motor
        self.__rodas = rodas

    @property
    def motor(self) -> str:
        return self.__motor

    @motor.setter
    def motor(self, novo_motor: str) -> None:
        self.__motor = novo_motor

    @property
    def rodas(self) -> str:
        return self.__rodas

    @rodas.setter
    def rodas(self, novas_rodas: str) -> None:
        self.__rodas = novas_rodas

    def __repr__(self) -> str:
        representacao = Transporte.__repr__(self)
        representacao += f'Motor: {self.__motor}\n'
        representacao += f'Rodas: {self.__rodas}\n'
        return representacao
