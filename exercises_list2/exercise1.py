import random

vector = []
for i in range(5):
    vector.append(random.randint(0, 100))

for i in range(len(vector)):
    if vector[i] == vector[-1]:
        print(vector[i], end='')
    else:
        print(vector[i], end=', ')
