# 1)
class Televisao:
    def __init__(self):
        self.__ligada = False
        self.__canal = 2

# 2)
class Televisao:
    def __init__(self, tamanho, marca):
        self.__ligada = False
        self.__canal = 2
        self.__tamanho = tamanho
        self.__marca = marca
    
    def get_atributes(self):
        return f'{self.__tamanho} {self.__marca}'

tv1 = Televisao('Samsung', '32')
tv2 = Televisao('Sony', '43')
print(tv1.get_atributes(), tv2.get_atributes())

# 3)
class Televisao:
    def __init__(self, tamanho, marca, canal_inicial):
        self.__ligada = False
        self.__canal = canal_inicial
        self.__tamanho = tamanho
        self.__marca = marca

    def get_atributes(self):
        return f'{self.__tamanho} {self.__marca} {self.__canal}'

    def mudar_canal_para_cima(self):
        self.__canal += 1

    def mudar_canal_para_baixo(self):
        self.__canal -= 1

# 4)
class Televisao:
    def __init__(self, tamanho, marca, canal_inicial):
        self.__ligada = False
        self.__canal_minimo = 1
        self.__canal_maximo = 99
        self.__canal = canal_inicial
        self.__tamanho = tamanho
        self.__marca = marca

    def get_atributes(self):
        return f'{self.__tamanho} {self.__marca} {self.__canal}'

    def mudar_canal_para_cima(self):
        if self.__canal == self.__canal_maximo:
            self.__canal = self.__canal_minimo
        else:
            self.__canal += 1

    def mudar_canal_para_baixo(self):
        if self.__canal == self.__canal_minimo:
            self.__canal = self.__canal_maximo
        else:
            self.__canal -= 1

# 5)
class Televisao:
    def __init__(self, tamanho, marca, canal_inicial, canal_minimo=2, canal_maximo=14):
        self.__ligada = False
        self.__canal_minimo = canal_minimo
        self.__canal_maximo = canal_maximo
        self.__canal = canal_inicial
        self.__tamanho = tamanho
        self.__marca = marca

    def get_atributes(self):
        return f'{self.__tamanho} {self.__marca} {self.__canal}'

    def mudar_canal_para_cima(self):
        if self.__canal == self.__canal_maximo:
            self.__canal = self.__canal_minimo
        else:
            self.__canal += 1

    def mudar_canal_para_baixo(self):
        if self.__canal == self.__canal_minimo:
            self.__canal = self.__canal_maximo
        else:
            self.__canal -= 1

# 6)
class Televisao:
    def __init__(self, tamanho, marca, canal_inicial, canal_minimo=2, canal_maximo=14):
        self.__ligada = False
        self.__canal_minimo = canal_minimo
        self.__canal_maximo = canal_maximo
        self.__canal = canal_inicial
        self.__tamanho = tamanho
        self.__marca = marca

    def get_atributes(self):
        return f'{self.__tamanho} {self.__marca} {self.__canal} {self.__canal_minimo} {self.__canal_maximo}'

    def mudar_canal_para_cima(self):
        if self.__canal == self.__canal_maximo:
            self.__canal = self.__canal_minimo
        else:
            self.__canal += 1

    def mudar_canal_para_baixo(self):
        if self.__canal == self.__canal_minimo:
            self.__canal = self.__canal_maximo
        else:
            self.__canal -= 1

tv1 = Televisao('43', 'Samsung', 5, canal_minimo=1, canal_maximo=20)
print(tv1.get_atributes())
tv2 = Televisao('32', 'Sony', 10, canal_minimo=3, canal_maximo=50)
print(tv2.get_atributes())

# 7)
class Cidade:
    def __init__(self, nome, populacao):
        self.__nome = nome
        self.__populacao = populacao

    def ver_populacao_da_cidade(self):
        return self.__populacao

    def ver_nome(self):
        return self.__nome

class Estado:
    def __init__(self, nome, sigla, *cidades):
        self.__nome = nome
        self.__sigla = sigla
        self.__cidades = cidades

    def calcular_populacao_total(self):
        populacao_total = 0
        for cidade in self.__cidades:
            populacao_total += cidade.ver_populacao_da_cidade()
        return populacao_total

    def ver_cidades(self):
        cidades_info = []
        for cidade in self.__cidades:
            cidades_info.append(f'{cidade.ver_nome()} {cidade.ver_populacao_da_cidade()}')
        return '\n'.join(cidades_info)

florianopolis = Cidade('Florianópolis', 300)
chapeco = Cidade('Chapecó', 150)
santa_catarina = Estado('Santa Catarina', 'SC', florianopolis, chapeco)

belo_horizonte = Cidade('Belo Horizonte', 300)
uberlandia = Cidade('Uberlândia', 170)
minas_gerais = Estado('Minas Gerais', 'MG', belo_horizonte, uberlandia)

manaus = Cidade('Manaus', 180)
manacapuru = Cidade('Manacapuru', 100)
amazonas = Estado('Amazonas', 'AM', manaus, manacapuru)

print(santa_catarina.ver_cidades())
print(santa_catarina.calcular_populacao_total())

print(minas_gerais.ver_cidades())
print(minas_gerais.calcular_populacao_total())

print(amazonas.ver_cidades())
print(amazonas.calcular_populacao_total())

# 8)
import math
class Coordenada:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def mostrar_coordenadas(self):
        return f'{self.__x} {self.__y}'

    def calcular_distancia(self, coordenada_a_comparar):
        x1, y1 = map(int, [self.__x, self.__y])
        x2, y2 = map(int, coordenada_a_comparar.mostrar_coordenadas.split())
        distancia_entre_os_pontos = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distancia_entre_os_pontos

    def coordenada_polar(self):
        magnitude = self.calcular_distancia(Coordenada(0, 0))
        
        if self.__x > 0:
            angulo = math.degrees(math.atan(self.__y / self.__x))
        elif self.__x < 0:
            angulo = 180 + math.degrees(math.atan(self.__y / self.__x))
        elif self.__x == 0 and self.__y > 0:
            angulo = 90
        elif self.__x == 0 and self.__y < 0:
            angulo = -90
        else:
            angulo = 0
        
        return f'{magnitude}∠{angulo:.2f}°'

coordenada1 = Coordenada(4, 6)
coordenada2 = Coordenada(10, 18)
print(coordenada1.mostrar_coordenadas)
print(coordenada2.mostrar_coordenadas)

print(coordenada1.calcular_distancia(coordenada2))
print(coordenada1.coordenada_polar())

# 9)
class Quadrado:
    def __init__(self, lado):
        self.__lado = lado

    def calcular_area(self):
        return self.__lado**2

    def calcular_perimetro(self):
        return self.__lado * 4

    @property
    def lado(self):
        return self.__lado


class Retangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def calcular_area(self):
        return self.__base * self.__altura

    def calcular_perimetro(self):
        return 2 * (self.__base + self.__altura)

    @property
    def base(self):
        return self.__base

    @property
    def altura(self):
        return self.__altura


class Circulo:
    def __init__(self, raio):
        self.__raio = raio

    def calcular_area(self):
        return math.pi * self.__raio ** 2

    def calcular_perimetro(self):
        return math.pi * self.__raio * 2

    @property
    def raio(self):
        return self.__raio

    @property
    def diametro(self):
        return self.__raio * 2


formas = [
    Quadrado(4),
    Retangulo(10, 7),
    Circulo(3)
]

for forma in formas:
    print(f'Area: {forma.calcular_area()}\nPerimetro: {forma.calcular_perimetro()}')

# 10)
class Fracao:
    def __init__(self, numerador:int, denominador:int):
        self.__numerador = numerador
        self.__denominador = denominador

    def somar(self, fracao_a_ser_somada):
        pass

    @property
    def numerador(self):
        return self.__numerador
    
    @property
    def denominador(self):
        return self.__denominador