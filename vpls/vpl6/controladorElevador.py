from abstractControladorElevador import AbstractControladorElevador
from elevador import Elevador
from comandoInvalidoException import ComandoInvalidoException

class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        super().__init__()
        self.__elevador = Elevador(0, 0, 0, 0)

    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    def subir(self) -> str:
        return self.__elevador.subir()

    def descer(self) -> str:
        return self.__elevador.descer()

    def entraPessoa(self) -> str:
        return self.__elevador.entraPessoa()

    def saiPessoa(self) -> str:
        return self.__elevador.saiPessoa()

    def inicializarElevador(self, andarAtual: int, totalAndaresPredio: int, capacidade: int, totalPessoas: int):
        verificar_tipo = [andarAtual, totalAndaresPredio, capacidade, totalPessoas]
        resultado = [atributo for atributo in verificar_tipo if isinstance(atributo, int) and atributo >= 0]
        if len(resultado) == 4 and andarAtual <= totalAndaresPredio - 1 and totalPessoas <= capacidade:
            self.__elevador = Elevador(andarAtual, totalAndaresPredio, capacidade, totalPessoas)
        else:
            raise ComandoInvalidoException
