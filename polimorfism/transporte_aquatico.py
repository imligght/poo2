from transporte import Transporte


class TransporteAquatico(Transporte):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: int, boca: int, calado: int):
        Transporte.__init__(self, nome, altura, comprimento, carga, velocidade)
        self.__boca = boca
        self.__calado = calado

    @property
    def boca(self) -> int:
        return self.__boca

    @boca.setter
    def boca(self, nova_boca: int):
        self.__boca = nova_boca

    @property
    def calado(self) -> int:
        return self.__calado

    @calado.setter
    def calado(self, novo_calado: int) -> None:
        self.__calado = novo_calado

    def __repr__(self) -> str:
        representacao = Transporte.__repr__(self)
        representacao += f'Boca: {self.__boca}m\n'
        representacao += f'Calado: {self.__calado}m\n'
        return representacao
