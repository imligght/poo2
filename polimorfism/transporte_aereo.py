from transporte import Transporte


class TransporteAereo(Transporte):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: int, autonomia: int, envergadura: int):
        Transporte.__init__(self, nome, altura, comprimento, carga, velocidade)
        self.__autonomia = autonomia
        self.__envergadura = envergadura

    @property
    def autonomia(self) -> int:
        return self.__autonomia

    @autonomia.setter
    def autonomia(self, nova_autonomia: int) -> None:
        self.__autonomia = nova_autonomia

    @property
    def envergadura(self) -> int:
        return self.__envergadura

    @envergadura.setter
    def envergadura(self, nova_envergadura: int) -> None:
        self.__envergadura = nova_envergadura

    def __repr__(self) -> str:
        representacao = Transporte.__repr__(self)
        representacao += f'Autonomia: {self.__autonomia}km\n'
        representacao += f'Envergadura: {self.__envergadura}m\n'
        return representacao
