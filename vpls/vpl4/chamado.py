from abstractChamado import AbstractChamado
from tipoChamado import TipoChamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class Chamado(AbstractChamado):
    def __init__(
            self,
            data: Date,
            cliente: Cliente,
            tecnico: Tecnico,
            titulo: str,
            descricao: str,
            prioridade: int,
            tipo: TipoChamado):
        self.__data = data
        self.__cliente = cliente
        self.__tecnico = tecnico
        self.__titulo = titulo
        self.__descricao = descricao
        self.__prioridade = prioridade
        self.__tipo = tipo

    @property
    def data(self):
        return self.__data

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def tecnico(self):
        return self.__tecnico

    @property
    def titulo(self):
        return self.__titulo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def prioridade(self):
        return self.__prioridade

    @property
    def tipo(self):
        return self.__tipo

    @data.setter
    def data(self, data: Date):
        self.__data = data

    @cliente.setter
    def cliente(self, cliente: Cliente):
        self.__cliente = cliente

    @tecnico.setter
    def tecnico(self, tecnico: Tecnico):
        self.__tecnico = tecnico

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @prioridade.setter
    def prioridade(self, prioridade: int):
        self.__prioridade = prioridade

    @tipo.setter
    def tipo(self, tipo: TipoChamado):
        self.__tipo = tipo

    def __eq__(self, other_object) -> bool:
        if isinstance(other_object, Chamado):
            return (
                self.data == other_object.data and
                self.cliente == other_object.cliente and
                self.tecnico == other_object.tecnico and
                self.tipo == other_object.tipo
            )
        return False
