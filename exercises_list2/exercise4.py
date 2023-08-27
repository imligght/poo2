vowels = ['a', 'e', 'i', 'o', 'u']
char_vector = input('Forneça os 10 caracteres separados por espaços: ').split()
consonants_vector = []

if len(char_vector) != 10:
    print('Favor fornecer exatamente 10 caracteres.')
else:
    for char in char_vector:
        if len(char) != 1 or not char.isalpha():
            print(f'O caractere {char} não é um caractere válido.')
        elif char not in vowels:
            consonants_vector.append(char)

print(f'{len(consonants_vector)} dos caracteres que você forneceu são consoantes, sendo elas: {consonants_vector}')
