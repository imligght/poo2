from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):
    def __init__(self, personagem: Personagem) -> None:
        self.__personagem = personagem

    @property
    def personagem(self) -> Personagem:
        return self.__personagem

    def valor_total_carta(self) -> int:
        valor_total = 0
        valor_total += self.__personagem.energia
        valor_total += self.__personagem.habilidade
        valor_total += self.__personagem.velocidade
        valor_total += self.__personagem.resistencia
        return valor_total
