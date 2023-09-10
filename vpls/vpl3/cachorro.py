from mamifero import Mamifero


class Cachorro(Mamifero):
    def __init__(self, volume_som=3, tamanho_passo=3):
        super().__init__(volume_som, tamanho_passo)

    def mover(self):
        return f'ANIMAL: DESLOCOU {self.tamanho_passo}'

    def produzir_som(self):
        return f'MAMIFERO: PRODUZ SOM: {self.volume_som} SOM: AU'

    def latir(self):
        return self.produzir_som()
