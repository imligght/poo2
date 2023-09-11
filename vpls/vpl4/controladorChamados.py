from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []
        self.__tipos_chamados = []

    @property
    def tipoChamados(self) -> list:
        return self.__tipos_chamados

    def totalChamadosPorTipo(self, tipo: TipoChamado) -> int:
        count = 0
        for chamado in self.__chamados:
            if tipo == chamado.tipo:
                count += 1
        return count

    def incluiChamado(self,
                      data: Date,
                      cliente: Cliente,
                      tecnico: Tecnico,
                      titulo: str,
                      descricao: str,
                      prioridade: int,
                      tipo: TipoChamado) -> Chamado:

        if (isinstance(data, Date) and
            isinstance(cliente, Cliente) and
            isinstance(tecnico, Tecnico) and
            isinstance(titulo, str) and
            isinstance(descricao, str) and
            isinstance(prioridade, int) and
            isinstance(tipo, TipoChamado)
            ):
            chamado = Chamado(data,
                              cliente,
                              tecnico,
                              titulo,
                              descricao,
                              prioridade,
                              tipo)
            call_already_exists = False
            for call in self.__chamados:
                if call == chamado:
                    call_already_exists = True
                    break
            if not call_already_exists:
                self.__chamados.append(chamado)
            return chamado

    def incluiTipoChamado(self,
                          codigo: int,
                          nome: str,
                          descricao: str) -> TipoChamado:
        tipo_chamado = TipoChamado(codigo, descricao, nome)
        code_already_exists = False
        for call_type in self.__tipos_chamados:
            if call_type.codigo == tipo_chamado.codigo:
                code_already_exists = True
                break
        if not code_already_exists:
            self.__tipos_chamados.append(tipo_chamado)
        return tipo_chamado
