vector = list(map(float, input('Digite aqui as quatro notas separadas por um espaço: ').split()))

if len(vector) != 4:
    print('Favor inserir exatamente quatro notas.')
else:
    average = sum(vector) / len(vector)
    print('Notas fornecidas: ', vector)
    print('Média das notas: ', average)
