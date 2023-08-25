import random
# esta classe serve para modelar as cartas
class Card:
    def __init__(self, naipe:str, value:str):
        self.__naipe = naipe
        self.__value = value

    @property
    def naipe(self):
        return self.__naipe

    @property
    def value(self):
        return self.__value

    @naipe.setter
    def naipe(self, new_naipe):
        self.__naipe = new_naipe

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def __repr__(self):
        if self.__naipe.lower() == 'ouros':
            return f'♦ {self.__naipe.title()}, {self.__value.title()}'

        elif self.__naipe.lower() == 'paus':
            return f'♣ {self.__naipe.title()}, {self.__value.title()}'

        elif self.__naipe.lower() == 'copas':
            return f'♥ {self.__naipe.title()}, {self.__value.title()}'

        elif self.__naipe.lower() == 'espadas':
            return f'♠ {self.__naipe.title()}, {self.__value.title()}'

# esta classe serve para agrupar cartas, formando um deck
class Deck:
    def __init__(self, deck:list[Card]):
        self.__deck = deck

    @property
    def deck(self):
        return self.deck

    @deck.setter
    def deck(self, new_deck):
        self.__deck = new_deck

    def shuffle(self):
        random.shuffle(self.__deck)

    def buy_card(self, card:Card):
        self.__deck.append(card)

    def play_card(self, index:int):
        self.__deck.pop(index)

    def __repr__(self):
        deck_str = ''
        for card in self.__deck:
            deck_str += card.naipe + ' '
            deck_str += card.value + ', '
        return deck_str


# caso de teste
naipes = ['Ouros', 'Paus', 'Copas', 'Espadas']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']

cards = []
for _ in range(9):
    naipe = random.choice(naipes)
    value = random.choice(values)
    card = Card(naipe, value)
    cards.append(card)

for card in cards:
    print(card)


deck1 = Deck(cards)
print(deck1)
