students_grades_dict = {}

while True:
    student = input('Insira o nome do estudante: ')
    if student == '':
        break
    grades = list(map(float, input('Insira as duas notas do aluno, separadas por um espaço: ').split()))

    students_grades_dict[student] = grades

def calculate_grade():
    while True:
        name = input('Insira o nome do aluno que deseja calcular a média (ou pressione ENTER para sair): ')
        if name == '':
            break
        grades = students_grades_dict.get(name)
        if grades == None:
            print('Aluno não encontrado')
        else:
            average = sum(grades) / len(grades)
            print(f'A média das notas do aluno é: {average}')

# chamando a função que calcula a média do aluno e mostrando na tela
print(calculate_grade())
