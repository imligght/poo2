import random

vector = []
for i in range(5):
    vector.append(random.randint(0, 100))

print(f'Números: {vector}')
print(f'Soma do vetor: {sum(vector)}')

mult_result = 1
for i in range(len(vector)):
    mult_result *= vector[i]
print(f'Multiplicação do vetor: {mult_result}')
