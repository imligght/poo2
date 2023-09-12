from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, nome: str, altura: float, comprimento: float, carga: float, velocidade: int):
        self.__nome = nome
        self.__altura = altura
        self.__comprimento = comprimento
        self.__carga = carga
        self.__velocidade = velocidade

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self.__nome = novo_nome

    @property
    def altura(self) -> float:
        return self.__altura

    @altura.setter
    def altura(self, nova_altura: float) -> None:
        self.__altura = nova_altura

    @property
    def comprimento(self) -> float:
        return self.__comprimento

    @comprimento.setter
    def comprimento(self, novo_comprimento: float) -> None:
        self.__comprimento = novo_comprimento

    @property
    def carga(self) -> float:
        return self.__carga

    @carga.setter
    def carga(self, nova_carga: float) -> None:
        self.__carga = nova_carga

    @property
    def velocidade(self) -> int:
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, nova_velocidade: int) -> None:
        self.__velocidade = nova_velocidade

    @abstractmethod
    def __repr__(self) -> str:
        representacao = f''
        representacao += f'Objeto pertencente a classe: {self.__class__.__name__}\n'
        representacao += f'Nome: {self.__nome}\n'
        representacao += f'Altura: {self.__altura:.2f}m\n'
        representacao += f'Comprimento: {self.__comprimento:.2f}m\n'
        representacao += f'Carga: {self.__carga:.2f}t\n'
        representacao += f'Velocidade: {self.__velocidade}km/h\n'
        return representacao
