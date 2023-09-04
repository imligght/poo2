class NumbersBook:
    def __init__(self):
        self.__contacts = {}

    def add_new_name(self, name: str, *telephone):
        if name in self.__contacts:
            confirmation = input('O nome informado já existe na sua agenda, deseja adicionar o(s) novo(s) número(s) a tal pessoa? [y/n] ')
            if confirmation.lower() == 'y':
                self.__contacts[name].extend(telephone)
            else:
                pass
        else:
            self.__contacts[name] = list(telephone)

    def add_telephone(self, name, *telephone):
        if name in self.__contacts:
            self.__contacts[name].extend(telephone)
        else:
            confirmation = input('O nome que você informou ainda não existe nos contatos. Deseja adicioná-lo? [y/n] ')
            if confirmation.lower() == 'y':
                self.add_new_name(name, *telephone)
            else:
                pass

    def delete_telephone(self, telephone):
        for name, numbers in list(self.__contacts.items()):
            if telephone in numbers:
                numbers.remove(telephone)
                if not numbers:
                    del self.__contacts[name]

    def delete_name(self, name):
        for names in list(self.__contacts.keys()):
            if name in names:
                del self.__contacts[name]

    def consult_telephones(self, name):
        for names in self.__contacts.keys():
            if name in names:
                return f'O(s) número(s) de {name.title()} registrados são: {self.__contacts[name]}'
            else:
                return f'{name.title()} não encontrado na agenda.'

    def __repr__(self) -> str:
        representation = '\nNúmeros na agenda:\n'
        for name, numbers in self.__contacts.items():
            representation += f'{name.title()}: {numbers}\n'
        return representation


my_number_book = NumbersBook()
my_number_book.add_telephone('samanta', '75372634289', '7845637548')
my_number_book.add_new_name('samanta', '17273947828')
my_number_book.add_telephone('samanta', '48749392039')
my_number_book.add_telephone('samanta', '7348974270', '7582634984')
my_number_book.delete_telephone('7845637548')
my_number_book.add_new_name('donnie', '28064212')
print(my_number_book)
print(my_number_book.consult_telephones('samanta'))
my_number_book.delete_name('samanta')
print(my_number_book)
