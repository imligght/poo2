from Carta import *
from AbstractJogador import *
import random


class Jogador(AbstractJogador):
    def __init__(self,  nome: str) -> None:
        self.__nome = nome
        self.__mao = []

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def mao(self) -> list:
        return self.__mao

    @mao.setter
    def mao(self, mao) -> None:
        self.__mao = mao

    def baixa_carta_da_mao(self) -> Carta:
        carta_jogada = self.__mao[random.randint(0, len(self.__mao)-1)]
        self.__mao.remove(carta_jogada)
        return carta_jogada


    def inclui_carta_na_mao(self, carta: Carta) -> None:
        self.__mao.append(carta)
