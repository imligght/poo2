class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao
        
    def ver_informações(self):
        print(f'Cidade: {self.nome}')
        print(f'População: {self.populacao}')
        print()
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
cidade4 = Cidade('Blumenau', 45)
cidade5 = Cidade('Chapecó', 30)
cidade1.ver_informações()
cidade2.ver_informações()
cidade3.ver_informações()

estado1 = Estado('Santa Catarina', 'SC')
estado1.adicionar_cidade(cidade1)
estado1.adicionar_cidade(cidade4)
estado1.adicionar_cidade(cidade5)
estado2 = Estado('São Paulo', 'SP')
estado2.adicionar_cidade(cidade2)
estado3 = Estado('Califórnia', 'CA')
estado3.adicionar_cidade(cidade3)
estado1.mostrar_informacoes_do_estado()
print(estado1.calcular_populacao_total())
estado2.mostrar_informacoes_do_estado()
estado3.mostrar_informacoes_do_estado()