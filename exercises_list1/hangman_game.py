class HangMan:

    def __init__(self, word:str):
        self.__word = word
        self.__gallow = self.draw_gallow()
        self.__tempted_letter = ''
        self.__attempts_left = 6

    @property
    def draw_doll(self):
        if self.__attempts_left == 6:
            pass

    @property
    def attempts_left(self):
        return self.__attempts_left

    @property
    def gallow(self):
        return self.__gallow

    @property
    def word(self):
        return self.__word

    @property
    def lenght(self):
        return len(self.__word)

    def draw_gallow(self):
        gallow = ''
        for _ in range(self.lenght):
            gallow += '_'
        self.__gallow = gallow
        return self.__gallow

    def draw_letter_in_position(self, position:int):
        gallow_list = list(self.__gallow)  # Convertendo a string em uma lista mutável
        gallow_list[position] = self.__tempted_letter
        self.__gallow = ''.join(gallow_list)  # Convertendo a lista de volta para uma string
        return self.__gallow
    
    def trying(self, tempted_letter:str):
        self.__tempted_letter = tempted_letter
        if self.__tempted_letter not in self.word:
            self.__attempts_left -= 1
        else:
            for i, letter in enumerate(self.__word):
                if tempted_letter == letter:
                    self.draw_letter_in_position(i)
        self.won()
        self.lost()
                

    def won(self):
        if not '_' in self.__gallow:
            self.won_finish()

    def lost(self):
        if self.__attempts_left <= 0:
            self.lost_finish()

    def won_finish(self):
        won_message = 'Parabéns carinha, você ganhou! Toma uma frô:🌸'
        print(won_message)

    def lost_finish(self):
        lost_message = 'Ah, você perdeu, que chato. Mas não desanima não mano *soquinho*👊'
        print(lost_message)

# iniciando uma partida com 'banana' sendo a palavra secreta
hangman1 = HangMan('banana')
# tentativas do jogador, neste exemplo o jogador perde
hangman1.trying('b')
hangman1.trying('i')
hangman1.trying('o')
hangman1.trying('a')
hangman1.trying('u')
hangman1.trying('j')
hangman1.trying('r')
# comente a próxima linha e descomente a seguinte para ver um exemplo em que o jogador ganha
hangman1.trying('m')
#hangman1.trying('n')
print(hangman1.gallow)
print(hangman1.attempts_left)