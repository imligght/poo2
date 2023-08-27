numbers_vector = list(map(int, input('Insira aqui os dez números separados por espaços: ').split()))
squares_sum = 0

for i in numbers_vector:
    squares_sum += i ** 2

print('A soma dos quadrados dos números lidos é ', squares_sum)
