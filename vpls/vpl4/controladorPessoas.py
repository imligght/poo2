from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
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
        client_already_exists = False
        for client in self.__clientes:
            if client.codigo == cliente.codigo:
                client_already_exists = True
                break
        if not client_already_exists:
            self.__clientes.append(cliente)
        return cliente

    def incluiTecnico(self, codigo: int, nome: str) -> Tecnico:
        tecnico = Tecnico(nome, codigo)
        technician_already_exists = False
        for technician in self.__tecnicos:
            if technician.codigo == tecnico.codigo:
                technician_already_exists = True
                break
        if not technician_already_exists:
            self.__tecnicos.append(tecnico)
        return tecnico
