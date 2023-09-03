from abc import ABC, abstractmethod

class NumberBook(ABC):
    def __init__(self):
        self.__contacts = {}

    @abstractmethod
    def add_new_name(self, name):
        pass

    @abstractmethod
    def add_telephone(self, name, telephone):
        pass

    @abstractmethod
    def delete_telephone(self, telephone):
        pass

    @abstractmethod
    def delete_name(self, name):
        pass

    @abstractmethod
    def consult_telephone(self, name):
        pass
