from transporte import Transporte
from transporte_aereo import TransporteAereo
from transporte_terrestre import TransporteTerreste
from transporte_aquatico import TransporteAquatico


class Catalogo:
    def __init__(self) -> None:
        self.__transportes_cadastrados = []

    def cadastrar_transporte(self, objeto_transporte: Transporte) -> None:
        if not isinstance(objeto_transporte, Transporte):
            return

        self.__transportes_cadastrados.append(objeto_transporte)

    def apresentar_transportes_cadastrados(self) -> str:
        apresentacao = f''
        for transporte in self.__transportes_cadastrados:
            apresentacao += f'{transporte}\n'
        return apresentacao

# criando um caso de teste para cada classe concreta
ex_transporte_aereo = TransporteAereo('aviao', 100.0, 10.0, 1000.0, 100, 50, 30)
ex_transporte_terrestre = TransporteTerreste('carro', 2.0, 5.0, 30.0, 200, 'v8', 'rodas michelin')
ex_transporte_aquatico = TransporteAquatico('barco', 10.0, 30.0, 100.0, 100, 30, 20)

ex_catalogo = Catalogo()

ex_transportes = [
    ex_transporte_aereo,
    ex_transporte_terrestre,
    ex_transporte_aquatico
]

# cadastrando cada instancia no catalogo
for transporte in ex_transportes:
    ex_catalogo.cadastrar_transporte(transporte)

# printando na tela a representacao do catalogo
print(ex_catalogo.apresentar_transportes_cadastrados())
