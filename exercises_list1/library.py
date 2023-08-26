class Stock:
    def __init__(self):
        self.__avaliable_books = []
        self.__borrowed_books = []

    @property
    def all_books(self):
        if len(self.__avaliable_books) == 0 and len(self.__borrowed_books) == 0:
            return f'Nenhum livro encontrado.\n'
        else:
            all_books = []
            for book in self.__avaliable_books:
                all_books.append(book.title)
            for book in self.__borrowed_books:
                all_books.append(book.title)
        all_books = '\n'.join(all_books)
        return f'Todos os livros da biblioteca:\n{all_books}\n'

    @property 
    def avaliable_books(self):
        if len(self.__avaliable_books) == 0:
            return f'Não temos nenhum livro disponível no momento.\n'
        else:
            avaliable_books = []
            for book in self.__avaliable_books:
                avaliable_books.append(book.title)
            avaliable_books = '\n'.join(avaliable_books)
            return f'Estes são os livros disponíveis no momento:\n{avaliable_books}\n'

    @property
    def borrowed_books(self):
        if len(self.__borrowed_books) == 0:
            return f'Nenhum livro emprestado no momento.\n'
        else:
            borrowed_books = []
            for book in self.__borrowed_books:
                borrowed_books.append(book.title)
            borrowed_books = '\n'.join(borrowed_books)
            return f'Livros emprestados:\n{borrowed_books}\n'

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

    # não entendi o que queria dizer "(outro software)" no enunciado da questão
    # então acabei fazendo um simples método para realizar as buscas de livros
    def search(self, search_method:str, search:str):
        if search_method.lower() == 'titulo':
            occurrences = 0
            for book in self.__avaliable_books:
                if search.title() == book.title:
                    occurrences += 1
            for book in self.__borrowed_books:
                if search.title() == book.title:
                    occurrences += 1
            if occurrences == 0:
                return f'Não temos exemplares do livro {search.title()} disponibilizados na biblioteca no momento.\n'
            else:
                return f'Temos {occurrences} exemplar(es) de {search.title()} na biblioteca!\n'

        elif search_method.lower() == 'autor':
            occurrences = 0
            books = []
            for book in self.__avaliable_books:
                if book.author == search.title():
                    occurrences += 1
                    books.append(book.title)
            for book in self.__borrowed_books:
                if book.author == search:
                    occurrences += 1
                    books.append(book.title)
            books = '\n'.join(books)
            if occurrences == 0:
                return f'Não temos nenhum livro de {search.title()} disponibilizados na biblioteca no momento.\n'
            else:
                return f'Temos {occurrences} livro(s) de {search.title()} na biblioteca! São eles:\n{books}\n'


class Book:
    def __init__(self, title, author, year, publishing_company, edition, volume):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__publishing_company = publishing_company
        self.__edition = edition
        self.__volume = volume

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year

    @property
    def publishing_company(self):
        return self.__publishing_company

    @property
    def edition(self):
        return self.__edition

    @property
    def volume(self):
        return self.__volume

    
book_1 = Book('Alice In Wonderland', 'Lewis Carroll', '1865', 'Editora do Brasil S/A', 'First Edition', 'Volume 2')
book_2 = Book('The Little Prince', 'Antoine de Saint-Exupéry', '1943', 'Reynal & Hitchcock', 'Deluxe Edition', 'Volume 3')
book_3 = Book('The Universe In A Nutshell', 'Stephen Hawking', '2001', 'Editora do Brasil S/A', 'Deluxe Edition', 'Volume 4')
library_stock = Stock()

library_stock.add_book(book_1)
library_stock.add_book(book_2)
library_stock.add_book(book_3)

library_stock.borrow_book(book_1)
print(library_stock.search('autor', 'stephEn hAWKing'))
print(library_stock.search('tItulo', 'tHE liTtLe pRIncE'))
print(library_stock.search('auTor', 'Lewis Carroll'))


print(library_stock.all_books)
print(library_stock.borrowed_books)
print(library_stock.avaliable_books)
