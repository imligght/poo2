from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        super().__init__()
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    def incluiCliente(self, codigo: int, nome: str) -> Cliente:
        cliente = Cliente(nome, codigo)
        if cliente not in self.__clientes:
            self.__clientes.append(cliente)
        return cliente

    def incluiTecnico(self, codigo: int, nome: str) -> Tecnico:
        tecnico = Tecnico(nome, codigo)
        if tecnico not in self.__tecnicos:
            self.__tecnicos.append(tecnico)
        return tecnico
