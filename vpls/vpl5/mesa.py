from AbstractMesa import *


class Mesa(AbstractMesa):
    def __init__(self, jogador1: Jogador, jogador2: Jogador,
                 cartaJogador1: Carta, cartaJogador2: Carta) -> None:
        self.__jogador1 = jogador1
        self.__jogador2 = jogador2
        self.__cartaJogador1 = cartaJogador1
        self.__cartaJogador2 = cartaJogador2

    @property
    def jogador1(self) -> Jogador:
        return self.__jogador1

    @jogador1.setter
    def jogador1(self, jogador1: Jogador) -> None:
        self.__jogador1 = jogador1

    @property
    def jogador2(self) -> Jogador:
        return self.__jogador2

    @jogador2.setter
    def jogador2(self, jogador2: Jogador) -> None:
        self.__jogador2 = jogador2

    @property
    def carta_jogador1(self) -> Carta:
        return self.__cartaJogador1

    @carta_jogador1.setter
    def carta_jogador1(self, cartaJogador1: Carta) -> None:
        self.__cartaJogador1 = cartaJogador1

    @property
    def carta_jogador2(self) -> Carta:
        return self.__cartaJogador2

    @carta_jogador2.setter
    def carta_jogador2(self, cartaJogador2: Carta):
        self.__cartaJogador2 = cartaJogador2
