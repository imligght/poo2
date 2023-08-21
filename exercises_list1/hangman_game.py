class SecretWord:

    def __init__(self, theme:str, word:str):
        self.__word = word
        self.__theme = theme

    @property
    def word(self):
        return self.__word

    @property
    def theme(self):
        return self.__theme


class Game:

    def __init__(self, secret_word_obj):
        self.__tempted_letter = ''
        self.__draw = ''
        self.__secret_word = secret_word_obj.word
        self.__secret_word_letters = [letter for letter in secret_word_obj.word]
        self.__hit_letters = []

    @property
    def hit_letters(self):
        return self.__hit_letters

    @property
    def letters(self):
        return self.__secret_word_letters

    @property
    def lenght(self):
        return len(self.__secret_word.word)

    @property
    def draw(self):
        return self.__draw


    def position(self):
        for letter in range(self.lenght):
            if letter == self.__secret_word[letter]:
                self.__draw = self.__tempted_letter

    def draw_word(self):
        word_lenght = len(self.letters)
        draw = ''
        for letter in range(word_lenght):
            draw += '_'
        return draw

    def hit(self):
        for letter in self.letters:
            self.letters.remove(letter)
            self.__hit_letters.append(letter)
        return self.__hit_letters

    def trying(self, letter):
        self.__tempted_letter = letter
        # verifico se a letra que o jogador solicitou está na lista das letras
        if self.__tempted_letter in self.__secret_word_letters:
            # se sim, começo um processo para ver se essa letra aparece mais de uma vez
            amount_letter_instances = 0
            for letter in range(self.lenght):
                if self.__tempted_letter in self.__secret_word_letters:
                    amount_letter_instances += 1
            for i in range(amount_letter_instances):
                self.position()

            
        







word1 = SecretWord('fruta', 'banana')
print(word1.word)
game1 = Game(word1)