class Student: 
  
    def __init__(self, name:str, registration:int): 
        self.__name = name 
        self.__registration = registration 

    def __repr__(self):
       return f'{name}'

    @property
    def name(self):
        return self.__name

    @property
    def registration(self):
        return self.__registration
  
class Classroom: 
  
    def __init__(self, class_id:str, students:list[Student]): 
         self.__class_id = class_id 
         self.__students_belonging_to_the_class = students 
  
        
    def __repr__(self): 
        representation = f'Turma: {self.class_id}\nAlunos na classe: {self.students_amount}\n' 
        for student in self.students_belonging_to_class: 
             representation += f'{student}\n' 
         return representation 

     def add_student_to_the_class(self):
         self.__students_belonging_to_the_class.append(self)
  
     @property 
     def students_belonging_to_class(self): 
         return self.__students_belonging_to_the_class 
  
     @students_belonging_to_class.setter 
     def students_belonging_to_class(self, new_students): 
         self.__students_belonging_to_the_class = new_students 
  
     @property 
     def class_id(self): 
         return self.__class_id 
  
     @property 
     def students_amount(self): 
         return len(self.__students_belonging_to_the_class)    
  
  
class Professor: 
  
     def __init__(self, name:str, discipline:str, *teaching_classes:Classroom): 
         self.__name = name 
         self.__discipline = discipline 
         self.__teaching_classes = [] 
  
     @property 
     def name(self): 
         return self.__name 
  
     @property 
     def discipline(self): 
         return self.__discipline
    

aluno1 = Student('Alex', 1)
aluno2 = Student('Bob', 2)
aluno3 = Student('David', 3)

lista_de_alunos_matriculados = [aluno1,
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

turma = Classroom('1A', lista_de_alunos_matriculados)

for aluno in alunos_a_serem_matriculados:
    turma.add_student_to_the_class()


print(turma)
