import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']
vector = []
for j in range(10):
    i = random.randint(0, 22)
    vector.append(alphabet[i])

consonants_in_vector = []
for i in range(len(vector)):
    if vector[i] not in vowels:
        consonants_in_vector.append(vector[i])

print(f'O vetor tem {len(consonants_in_vector)} consoantes. Sendo elas: {consonants_in_vector}')
