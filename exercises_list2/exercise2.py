vector = list(map(float, input('Digite aqui os 10 números separados por espaço: ').split()))

if len(vector) != 10:
    print('O vetor deve conter exatamente 10 números reais.')
else:
    print('Aqui está o vetor de números reais que você digitou: ', end='')
    print(vector)
