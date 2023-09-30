from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int) -> None:
        self.__andarAtual = andarAtual
        self.__totalAndaresPredio = totalAndaresPredio
        self.__capacidade = capacidade
        self.__totalPessoas = totalPessoas

    @property
    def andarAtual(self) -> int:
        return self.__andarAtual

    @andarAtual.setter
    def andarAtual(self, andarAtual: int) -> None:
        self.__andarAtual = andarAtual

    @property
    def totalAndaresPredio(self) -> int:
        return self.__totalAndaresPredio

    @totalAndaresPredio.setter
    def totalAndaresPredio(self, totalAndaresPredio: int) -> None:
        self.__totalAndaresPredio = totalAndaresPredio

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade: int) -> None:
        self.__capacidade = capacidade

    @property
    def totalPessoas(self) -> int:
        return self.__totalPessoas

    @totalPessoas.setter
    def totalPessoas(self, totalPessoas: int) -> None:
        self.__totalPessoas = totalPessoas

    def descer(self) -> str:
        if self.__andarAtual > 0:
            self.__andarAtual -= 1
            return f'Elevador foi para o {self.__andarAtual}.'
        else:
            raise ElevadorJahNoTerreoException

    def subir(self) -> str:
        if self.__andarAtual < self.__totalAndaresPredio - 1:
            self.__andarAtual += 1
            return f'Elevador foi para o {self.__andarAtual}'
        else:
            raise ElevadorJahNoUltimoAndarException

    def entraPessoa(self) -> str:
        if self.__totalPessoas < self.__capacidade:
            self.__totalPessoas += 1
            return f'Elevador está com {self.__totalPessoas} a bordo.'
        else:
            raise ElevadorCheioException

    def saiPessoa(self) -> str:
        if self.__totalPessoas > 0:
            self.__totalPessoas -= 1
            return f'Elevador está com {self.__totalPessoas} a bordo.'
        else:
            raise ElevadorJahVazioException
