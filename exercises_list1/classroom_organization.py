class Student:

    def __init__(self, name:str, registration:int):
        self.__name = name
        self.__registration = registration
        self.__grades = []
        self.__school_days = 250
        self.__missed_days = 0

    def calculate_frequency(self):
        frequency = ((self.school_days - self.__missed_days) / self.school_days) * 100
        return frequency
        

    def register_missed_days(self, missed_days):
        self.__missed_days = missed_days

    def register_grade(self, grades:list):
        for grade in grades:
            self.__grades.append(grade)

    def calculate_average(self):
        if len(self.__grades) == 0:
            return 0
        else:
            average = 0
            for grade in list(self.__grades):
                average += int(grade)
            average = average / len(self.__grades)
        return f'A média de {self.name} é {average:.1f}'

    @property
    def missed_days(self):
        return self.__missed_days

    @missed_days.setter
    def missed_days(self, missed_days):
        self.__missed_days = missed_days

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
        return f'Aluno(a): {__self.name}\nDias ausênte: {self.__missed_days}\nNotas: {self.__grades}'

class Classroom: 

    def __init__(self, class_id:str, teacher, students:list[Student]): 
        self.__class_id = class_id 
        self.__students_belonging_to_the_class = students 
        self.__teacher = teacher


    def __repr__(self):
        representation = f'Turma: {self.class_id}\nAlunos na classe: {self.students_amount}\n'
        for student in self.students_belonging_to_class:
            representation += f'\n{student}\n'
        return f'{representation}'

    def add_student_to_the_class(self, student:Student):
        self.__students_belonging_to_the_class.append(student)

    @property
    def teacher(self):
        return self.__teacher

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

    def __init__(self, name:str, discipline:str):
        self.__name = name
        self.__discipline = discipline

    def __repr__(self):
        return f'Nome: {self.name}\nDisciplina: {self.discipline}\n'

    @property 
    def name(self):
        return self.__name

    @property
    def discipline(self):
        return self.__discipline


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

# instanciei professores e printei os mesmos
professor_calc = Professor('Aaron', 'Cálculo')
professor_quim = Professor('Alana', 'Química')
print(professor_calc)
print(professor_quim)

# criando uma instancia de turma (classroom), que inicialmente contém três alunos
turma1 = Classroom('CALC1', professor_calc, lista_de_alunos_matriculados)
turma2 = Classroom('QUIM2', professor_quim, alunos_a_serem_matriculados)

# adicionando alunos à lista de uma turma. Alunos que entraram na metade de um ano, por vagas remanescentes, por exemplo.
for aluno in alunos_a_serem_matriculados:
    if aluno not in turma1.students_belonging_to_class:
        turma1.add_student_to_the_class(aluno)

lista_de_notas = [4.5, 7.5, 9.0]
# para fins de simplicidade e facilidade de compreensão, atribuí a mesma lista de notas para todos os alunos instanciados
# porém, elas sem problema algum poderiam ser nostas diferentes
aluno1.register_grade(lista_de_notas)
aluno2.register_grade(lista_de_notas)
aluno3.register_grade(lista_de_notas)
aluno4.register_grade(lista_de_notas)
aluno5.register_grade(lista_de_notas)
aluno6.register_grade(lista_de_notas)

aluno1.register_missed_days(10)

print(turma1)
print(turma2)

# criei um método que calcula a média das notas de um aluno
# exemplo de uso:
print(aluno1.calculate_average())
print(aluno1.calculate_frequency())
