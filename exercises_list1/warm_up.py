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
    
    @property
    def get_atributes(self):
        return f'Tamanho: {self.__tamanho}\nMarca: {self.__marca}'

tv1 = Televisao('Samsung', '32')
tv2 = Televisao('Sony', '43')
print(tv1.get_atributes, tv2.get_atributes)

# 3)
class Televisao:
    def __init__(self, tamanho, marca, canal_inicial):
        self.__ligada = False
        self.__canal = canal_inicial
        self.__tamanho = tamanho
        self.__marca = marca

    @property
    def get_atributes(self):
        return f'Tamanho: {self.__tamanho}\nTamanho: {self.__marca}\nCanal altual: {self.__canal}'

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

    @property
    def get_atributes(self):
        return f'Tamanho: {self.__tamanho}\nTamanho: {self.__marca}\nCanal altual: {self.__canal}'

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

    @property
    def get_atributes(self):
        return f'Tamanho: {self.__tamanho}\nTamanho: {self.__marca}\nCanal altual: {self.__canal}'

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

    @property
    def get_atributes(self):
        return f'Tamanho: {self.__tamanho}\nTamanho: {self.__marca}\nCanal altual: {self.__canal}\nCanal minimo: {self.__canal_minimo}\nCanal máximo:{self.__canal_maximo}'

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
print(tv1.get_atributes)
tv2 = Televisao('32', 'Sony', 10, canal_minimo=3, canal_maximo=50)
print(tv2.get_atributes)

# 7)
class Cidade:
    def __init__(self, nome, populacao):
        self.__nome = nome
        self.__populacao = populacao

    @property
    def ver_populacao_da_cidade(self):
        return self.__populacao

    @property
    def ver_nome(self):
        return f'{self.__nome}'

class Estado:
    def __init__(self, nome, sigla, *cidades):
        self.__nome = nome
        self.__sigla = sigla
        self.__cidades = cidades

    def calcular_populacao_total(self):
        populacao_total = 0
        for cidade in self.__cidades:
            populacao_total += int(cidade.ver_populacao_da_cidade)
        return f'\nPopulação total do estado:\n{populacao_total}'

    @property
    def nome_do_estado(self):
        return self.__nome

    @property
    def sigla_do_estado(self):
        return self.__sigla

    @property
    def ver_cidades(self):
        cidades_info = []
        for cidade in self.__cidades:
            cidades_info.append(f'{cidade.ver_nome} {cidade.ver_populacao_da_cidade}')
        cidades_pertencentes_ao_estado = '\n'.join(cidades_info)
        return f'Cidades pertencentes a {self.nome_do_estado} - {self.sigla_do_estado}:\n{cidades_pertencentes_ao_estado}'

florianopolis = Cidade('Florianópolis', 300)
chapeco = Cidade('Chapecó', 150)
santa_catarina = Estado('Santa Catarina', 'SC', florianopolis, chapeco)

belo_horizonte = Cidade('Belo Horizonte', 300)
uberlandia = Cidade('Uberlândia', 170)
minas_gerais = Estado('Minas Gerais', 'MG', belo_horizonte, uberlandia)

manaus = Cidade('Manaus', 180)
manacapuru = Cidade('Manacapuru', 100)
amazonas = Estado('Amazonas', 'AM', manaus, manacapuru)

estados = [
    santa_catarina,
    minas_gerais,
    amazonas
]

for estado in estados:
    print(estado.ver_cidades, estado.calcular_populacao_total())

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
    def __init__(self, numerador:int, denominador:int=1):
        self.__numerador = numerador
        self.__denominador = denominador

    def somar(self, fracao_a_ser_somada):
        if self.denominador == fracao_a_ser_somada.denominador:
            numerador = self.__numerador + fracao_a_ser_somada.__numerador
            return Fracao(numerador, self.denominador)
        else:
            mmc = math.lcm(self.__denominador, fracao_a_ser_somada.__denominador)
            novo_numerador = int((mmc / self.__denominador) * self.__numerador + (mmc / fracao_a_ser_somada.__denominador) * fracao_a_ser_somada.__numerador)
            self.__denominador = mmc
            return Fracao(novo_numerador, self.__denominador)

    def subtrair(self, fracao_a_ser_subtraida):
        if self.denominador == fracao_a_ser_subtraida.denominador:
            numerador = self.numerador - fracao_a_ser_subtraida.numerador
            return Fracao(numerador, self.denominador)
        else:
            mmc = math.lcm(self.denominador, fracao_a_ser_subtraida.denominador)
            novo_numerador = int((mmc / self.denominador) * self.numerador) - int((mmc / fracao_a_ser_subtraida.denominador) * fracao_a_ser_subtraida.numerador)
            self.denominador = mmc
            return Fracao(novo_numerador, self.denominador)

    def multiplicar(self, fracao_a_ser_multiplicada):
        self.numerador *= fracao_a_ser_multiplicada.numerador
        self.denominador *= fracao_a_ser_multiplicada.denominador
        return Fracao(self.numerador, self.denominador)

    def dividir(self, fracao_a_ser_dividida):
        novo_numerador = fracao_a_ser_dividida.inverter_fracao().numerador * self.numerador
        novo_denominador = fracao_a_ser_dividida.denominador * self.denominador
        return Fracao(novo_numerador, novo_denominador)

    def inverter_fracao(self):
        variavel_temporaria = self.numerador
        self.__numerador = self.__denominador
        self.__denominador = variavel_temporaria
        return self

    def calcular_valor_real(self):
        valor_real = f'{self.__numerador / self.__denominador}'
        return float(valor_real)

    def simplificar_fracao(self):
        max_divisor_comum = math.gcd(self.__numerador, self.__denominador)
        self.__numerador //= max_divisor_comum
        self.__denominador //= max_divisor_comum
        return self

    @classmethod
    def criar_fracao_a_partir_de_um_numero_real(cls, numero_real):
        numeros_apos_a_virgula = len(str(numero_real).split('.')[1])
        numerador = int(numero_real * 10 ** numeros_apos_a_virgula)
        denominador = int(10 ** numeros_apos_a_virgula)
        return cls(numerador, denominador)

    @property
    def mostrar_fracao(self):
        return f'{self.__numerador}/{self.__denominador}'

    @property
    def numerador(self):
        return self.__numerador

    @property
    def denominador(self):
        return self.__denominador

    @denominador.setter
    def denominador(self, novo_denominador):
        self.__denominador = novo_denominador

    @numerador.setter 
    def numerador(self, novo_numerador):
        self.__numerador = novo_numerador

    def __str__(self):
        return f'{self.__numerador}/{self.__denominador}'

fracao1 = Fracao(5, 3)
fracao2 = Fracao(3, 2)

print(fracao1.dividir(fracao2))
print(Fracao.criar_fracao_a_partir_de_um_numero_real(1.148491))
