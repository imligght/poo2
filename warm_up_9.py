class Quadrado:
    def __init__(self, lado):
        self.lado = lado 

    def calcular_area(self):
        return self.lado * 2

class Retangulo:
    def __init__(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento

    def calcular_area(self):
        return self.largura * self.comprimento

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * (self.raio**2)

quadrado = Quadrado(4)
print(quadrado.calcular_area())

retangulo = Retangulo(2, 6)
print(retangulo.calcular_area())

circulo = Circulo(4)
print(circulo.calcular_area())