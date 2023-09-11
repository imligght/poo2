from abstractTipoChamado import AbstractTipoChamado


class TipoChamado(AbstractTipoChamado):
    def __init__(self, codigo: int, descricao: str, nome: str):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def nome(self):
        return self.__nome

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    def __eq__(self, other_object) -> bool:
        if isinstance(other_object, TipoChamado):
            return (
                self.__codigo == other_object.__codigo
            )
        return False
