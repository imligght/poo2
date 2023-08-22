class Class:

    def __init__(self, class_id:str, students_amount:int):
        self.__class_id = class_id
        self.__students_amount = students_amount
        self.__students_amount = len(self.__students_belonging_to_the_class)
        self.__students_belonging_to_the_class = []

    def __repr__(self):
        return f'Turma: {self.class_id}\nAlunos na classe: {self.students_amount}\n'

    @property
    def class_id(self):
        return self.__class_id
    
    @property
    def students_amount(self):
        return self.__students_amount
    
    @property
    def students_amount(self):
        return len(self.__students_belonging_to_the_class)
    

class Professor:

    def __init__(self, name:str, discipline:str, *teaching_classes:Class):
        self.__name = name
        self.__discipline = discipline
        self.__teaching_classes = []

    @property
    def name(self):
        return self.__name
    
    @property
    def disciplime(self):
        return self.__discipline
    

class Student:

    def __init__(self, name:str, registration:int):
        self.__name = name
        self.__registration = registration

    