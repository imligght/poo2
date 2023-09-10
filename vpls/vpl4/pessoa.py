from abc import ABC, abstractmethod
from abstractPessoa import AbstractPessoa


class Pessoa(AbstractPessoa, ABC):
    def __init__(self, nome: str, codigo: int):
        self.__nome = nome
        self.__codigo = codigo

    @property
    @abstractmethod
    def nome(self) -> str:
        return self.__nome

    @property
    @abstractmethod
    def codigo(self) -> int:
        return self.__codigo
