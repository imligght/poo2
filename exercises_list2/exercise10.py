vector1 = input('Insira os dez elementos do primeiro vetor separados por espaços: ').split()
vector2 = input('Insira os dez elementos do segundo vetor separados por espaços: ').split()

print('Primeiro vetor lido: ', vector1)
print('Segundo vetor lido: ', vector2)

intercaleted_vector = []
for i in range(10):
    intercaleted_vector.append(vector1[i])
    intercaleted_vector.append(vector2[i])

print('Vetor intercalado: ', end='')
print(*intercaleted_vector, sep=', ')
