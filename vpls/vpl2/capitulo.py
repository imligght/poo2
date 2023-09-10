class Capitulo:
    def __init__(self, numero: int, titulo: str):
        self.__numero = numero
        self.__titulo = titulo

    def __eq__(self, other_chapter):
        if isinstance(other_chapter, Capitulo):
            return (
                self.__numero == other_chapter.numero and
                self.__titulo == other_chapter.titulo
            )
        return False

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
