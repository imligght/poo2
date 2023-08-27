counter = 0
average_vector = []

for i in range(10):
    counter += 1
    grades = list(map(int, input(f'Digite as quatro notas do {counter} aluno separadas por um espaço: ').split()))
    if len(grades) != 4:
        print('Favor fornecer as quatro notas.')
    else:
        average = sum(grades) / 4
        average_vector.append(average)

for i, average in enumerate(average_vector):
    if average >= 7:
        print(f'Aluno {i+1} teve uma média de {average}')
