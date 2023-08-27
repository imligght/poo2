vector = map(int, input("Digite aqui os cinco números, separados por um espaço: ").split())
print('Aqui estão os cinco números que você digitou: ', end='')
print(*vector, sep=', ', end='')
