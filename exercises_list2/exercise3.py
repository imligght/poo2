import random

vector = []
for i in range(4):
    vector.append(random.randint(0, 10))

average = sum(vector) / len(vector)
print(vector)
print(average)
