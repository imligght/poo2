from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora,
                 autor: Autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__capitulos = [Capitulo(numeroCapitulo, tituloCapitulo)]

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    @property
    def autores(self):
        return self.__autores

    def incluirAutor(self, autor: Autor):
        if autor not in self.__autores and isinstance(autor, Autor):
            self.__autores.append(autor)

    def excluirAutor(self, autor: Autor):
        self.__autores.remove(autor)

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        capitulo = Capitulo(numeroCapitulo, tituloCapitulo)
        already_exists = False
        for chapter in self.__capitulos:
            if capitulo == chapter:
                already_exists = True
                break
        if not already_exists:
            self.__capitulos.append(capitulo)

    def excluirCapitulo(self, tituloCapitulo: str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == tituloCapitulo:
                self.__capitulos.remove(capitulo)

    def findCapituloByTitulo(self, tituloCapitulo: str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == tituloCapitulo:
                return capitulo
