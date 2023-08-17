import math

class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar_coordenadas(self):
        print(f'{self.x}, {self.y}')

    def calcular_distancia(self, coordenada_para_comparar):
        distancia = ((coordenada_para_comparar.x - self.x)**2 + (coordenada_para_comparar.y - self.y)**2)**(1/2)
        return distancia
    
    def comparar_coordenadas(self):
        pass

    def mostrar_coordenada_polar(self):
        pass


coordenada1 = Coordenada(2, 4)
coordenada2 = Coordenada(4, 8)
print(coordenada1.calcular_distancia(coordenada2))

coordenada1.mostrar_coordenadas()