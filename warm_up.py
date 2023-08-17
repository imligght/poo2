# Criando classe televisao
class Televisao:
    def __init__(self, tamanho, marca, canal, canal_minimo=2, canal_maximo=14, ligada=False):
        self.tamanho = tamanho
        self.marca = marca
        self.ligada = ligada
        self.canal = canal
        self.canal_minimo = canal_minimo
        self.canal_maximo = canal_maximo
# Criei uma classe para mostrar os atributos, para facilitar a depuração
    def mostrar_atributos(self):
        print(f'Ligada' if self.ligada else 'Desligada')
        print(f'Canal: {self.canal}')
        print(f'Tamanho: {self.tamanho}')
        print(f'Marca: {self.marca}')
        print()
# Método para mudar canal (+)
    def muda_canal_para_cima(self):
        canal = self.canal
        canal_maximo = self.canal_maximo
        canal_minimo = self.canal_minimo

        if canal >= canal_maximo:
            canal = canal_minimo
        
        else:
            canal += 1

        self.canal = canal
# Método para mudar canal (-)
    def muda_canal_para_baixo(self):
        canal = self.canal
        canal_maximo = self.canal_maximo
        canal_minimo = self.canal_minimo

        if canal <= canal_minimo:
            canal = canal_maximo

        else:
            canal -= 1
        self.canal = canal
# Criando os dois objetos solicitados no exercício
tv1 = Televisao(32, 'Samsung', 2, canal_minimo=1, canal_maximo=15)
tv1.muda_canal_para_baixo()
tv1.mostrar_atributos()

tv2 = Televisao(42, 'LG', 14, canal_minimo=10, canal_maximo=100)
tv2.muda_canal_para_cima()
tv2.mostrar_atributos()


# 7)
class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao
        
    def ver_informações(self):
        print(self.nome)
        print(self.populacao)

class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []
    
    def adicionar_cidade(self, objeto_cidade):
        self.cidades.append(objeto_cidade)

    def calcular_populacao_total(self):
        return sum(cidade.populacao for cidade in self.cidades)

    def mostrar_informacoes_do_estado(self):
        print(f'Estado {self.nome} ({self.sigla})')
        print(f'Cidades pertencentes ao estado:')
        for i, cidade in enumerate(self.cidades):
            print(f'{i} - {cidade.nome}, População: {cidade.populacao}\n')

cidade1 = Cidade('Florianópolis', 100)
cidade2 = Cidade('São Paulo', 200)
cidade3 = Cidade('São Francisco', 300)
cidade1.ver_informações()