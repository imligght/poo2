import random

vector = []
for i in range(20):
    vector.append(random.randint(0, 100))

print(vector)
even_vector = []
odd_vector = []
for i in vector:
    if i % 2 == 0:
        even_vector.append(i)
    else:
        odd_vector.append(i)

print(f'Vetor de números pares: {even_vector}')
print(f'Vetor de números ímpares: {odd_vector}')
