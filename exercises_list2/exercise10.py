import random

vector1 = []
vector2 = []
for i in range(10):
    vector1.append(random.randint(0, 100))

for i in range(10):
    vector2.append(random.randint(0, 100))

print('Primeiro vetor gerado: ', vector1)
print('Segundo vetor gerado: ', vector2)

intercaleted_vector = []
for i in range(10):
    intercaleted_vector.append(vector1[i])
    intercaleted_vector.append(vector2[i])

print('Vetor intercalado: ', intercaleted_vector)
