class Stock:
    def __init__(self):
        self.__avaliable_books = []
        self.__borrowed_books = []
    
    def see_avaliable_books(self):
        if len(self.__avaliable_books) == 0:
            print("Não temos nenhum livro disponível no momento.")
        else:
            print(f'Estes são os livros dispiníveis no momento:')
            for book in self.__avaliable_books:
                print(book.get_title())
    def see_borrowed_books(self):
        if len(self.__borrowed_books) == 0:
            print("Nenhum livro emprestado no momento.")
        else:
            print("Estes são os livros emprestados no momento:")
            for book in self.__borrowed_books:
                print(book.get_title())

    def add_book(self, book):
        self.__avaliable_books.append(book)
        return self.__avaliable_books

    def borrow_book(self, book):
        if book in self.__avaliable_books:
            self.__avaliable_books.remove(book)
            self.__borrowed_books.append(book)
            return self.__borrowed_books

    def devolution(self, book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            self.__avaliable_books.append(book)
            return self.__avaliable_books

class Book:
    def __init__(self, title, author, year, publishing_company, edition, volume):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__publishing_company = publishing_company
        self.__edition = edition
        self.__volume = volume

    def get_title(self):
        return self.__title

book_1 = Book('Alice in Wonderland', 'Lewis Carroll', '1865', 'Editora do Brasil S/A', 'First Edition', 'Volume 2')
library_stock = Stock()

library_stock.add_book(book_1)
library_stock.see_avaliable_books()
library_stock.see_borrowed_books()

library_stock.borrow_book(book_1)
library_stock.see_avaliable_books()
library_stock.see_borrowed_books()


# Está ok, tudo funcionando, porém, falta adicionar um mecanismo de pesquisa, para que os usuários possam encontrar
# o livro que buscam pelo seu título, ou autor, ou ano, etc... Só não vou implementar agora porque não entendi o que quer dizer
# "outro software" no enunciado do exercício