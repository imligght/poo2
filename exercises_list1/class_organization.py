class Student: 
  
    def __init__(self, name:str, registration:int): 
        self.__name = name 
        self.__registration = registration
        self.__grades = list[float]
        self.__school_days = 250
        self.__frequency =  float

    @property
    def school_days(self):
        return self.__school_days
    
    @property
    def grades(self):
        return self.__grades

    @property
    def name(self):
        return self.__name

    @property
    def registration(self):
        return self.__registration
    
    def __repr__(self):
       return f'{self.name}'
  
class Classroom: 
  
    def __init__(self, class_id:str, students:list[Student]): 
        self.__class_id = class_id 
        self.__students_belonging_to_the_class = students 
  
        
    def __repr__(self): 
        representation = f'Turma: {self.class_id}\nAlunos na classe: {self.students_amount}\n' 
        for student in self.students_belonging_to_class: 
            representation += f'{student}\n' 
        return representation 

    def add_student_to_the_class(self, student:Student):
        self.__students_belonging_to_the_class.append(student)
  
    @property 
    def students_belonging_to_class(self): 
        return self.__students_belonging_to_the_class 
    # este setter pode ser utilizado quando um novo ano começar e a secretaria vá
    # trocar a lista de estudantes inteira
    @students_belonging_to_class.setter 
    def students_belonging_to_class(self, new_students:list[Student]):  
        self.__students_belonging_to_the_class = new_students 
  
    @property 
    def class_id(self): 
        return self.__class_id 
  
    @property 
    def students_amount(self): 
        return len(self.__students_belonging_to_the_class)    
  
  
class Professor: 
  
    def __init__(self, name:str, discipline:str, *teaching_classes:list[Classroom]): 
        self.__name = name 
        self.__discipline = discipline 
        self.__teaching_classes = teaching_classes
  
    @property 
    def name(self): 
        return self.__name 
  
    @property 
    def discipline(self): 
        return self.__discipline

    @property
    def teaching_classes(self):
        return self.__teaching_classes
    
# criando instancias de alunos para a realização de testes
aluno1 = Student('Alex', 1)
aluno2 = Student('Bob', 2)
aluno3 = Student('David', 3)

lista_de_alunos_matriculados = [
        aluno1,
        aluno2,
        aluno3
        ]

aluno4 = Student('Alan', 4)
aluno5 = Student('George', 5)
aluno6 = Student('John', 6)

alunos_a_serem_matriculados = [
        aluno4,
        aluno5,
        aluno6
        ]
# criando uma instancia de turma (classroom) chamada '1A', que inicialmente contém três alunos
turma = Classroom('1A', lista_de_alunos_matriculados)

# adicionando alunos à lista de uma turma. Alunos que entraram na metade de um ano, por vagas remanescentes, por exemplo.
for aluno in alunos_a_serem_matriculados:
    turma.add_student_to_the_class(aluno)


print(turma)