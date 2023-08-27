numbers_vector = list(map(int, input('Digite aqui os 20 números inteiros separados por espaços: ').split()))
even_vector = []
odd_vector = []

for number in numbers_vector:
    if len(numbers_vector) != 20:
        print('Favor fornecer exatamente 20 números.')
        break
    elif number % 2 == 0:
        even_vector.append(number)
    else:
        odd_vector.append(number)

print('Números pares: ', even_vector)
print('Números ímpares: ', odd_vector)
