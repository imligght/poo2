class Cliente:
    def __init__(self, nome:str, fone:str):
        self.__nome = nome
        self.__fone = fone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, fone):
        self.__fone = fone


class CategoriaProduto:
    def __init__(self, titulo:str):
        self.__titulo = titulo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo


class Produto:
    def __init__(self, codigo:int, descricao:str, categoria:str):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria = categoria
        self.__quantidade = 0
        self.__preco_unitario = 0.00
        self.__cliente = ''

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    def preco_total(self):
        return self.__quantidade * self.__preco_unitario
