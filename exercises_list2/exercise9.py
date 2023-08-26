import random

numbers_vector = []
for i in range(10):
    numbers_vector.append(random.randint(0, 50))
print('Vetor criado: ', numbers_vector)

result = 0
for i in numbers_vector:
    result += i ** 2
print('Soma dos quadrados dos elementos do vetor lido: ', result)
