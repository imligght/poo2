from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self) -> None:
        self.__baralho = []
        self.__personagens = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagens

    def inclui_personagem_na_lista(
        self,
        energia: int,
        habilidade: int,
        velocidade: int,
        resistencia: int,
        tipo: Tipo,
    ) -> Personagem:
        personagem = Personagem(energia, habilidade, velocidade, resistencia,
                                tipo)
        self.__personagens.append(personagem)
        return personagem

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        carta = Carta(personagem)
        self.__baralho.append(carta)
        return carta

    def iniciaJogo(self, jogador1: Jogador, jogador2: Jogador) -> None:
        for _ in range(5):
            jogador1.inclui_carta_na_mao(
                self.__baralho[random.randint(0, len(self.__baralho) - 1)]
            )
        for _ in range(5):
            jogador2.inclui_carta_na_mao(
                self.__baralho[random.randint(0, len(self.__baralho) - 1)]
            )

    def jogada(self, mesa: Mesa):
        total_pontos_jogador1 = mesa.carta_jogador1.valor_total_carta()
        total_pontos_jogador2 = mesa.carta_jogador2.valor_total_carta()

        vencedor_da_rodada = None
        if total_pontos_jogador1 > total_pontos_jogador2:
            vencedor_da_rodada = mesa.jogador1
            mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)
            mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador2)
            return vencedor_da_rodada

        elif total_pontos_jogador1 == total_pontos_jogador2:
            vencedor_da_rodada = None
            mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)
            mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
            return vencedor_da_rodada

        elif total_pontos_jogador1 < total_pontos_jogador2:
            vencedor_da_rodada = mesa.jogador2
            mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador1)
            mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
            return vencedor_da_rodada
