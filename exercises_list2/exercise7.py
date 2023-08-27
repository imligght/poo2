numbers = list(map(int, input('Insira aqui os 5 números separados por espaços: ').split()))

print(f'Soma dos números do vetor: {sum(numbers)}')

mult_result = 1
for number in numbers:
    mult_result *= number

print(f'Multiplicação dos números do vetor: {mult_result}')
