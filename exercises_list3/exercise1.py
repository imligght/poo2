def count_words_occurrences(text_file):
    words_dict = {}
    try:
        with open(text_file, 'r') as file:
            for line in file:
                line = line.strip().split()
                for word in line:
                    if word.isalpha():
                        first_letter = word[0].lower()
                        if first_letter in words_dict:
                            words_dict[first_letter].append(word)
                        else:
                            words_dict[first_letter] = [word]
    except Exception as e:
        print(str(e))

    amount_words_per_letter = []

    print('Esta é a quantidade de palavras iniciadas com cada letra:')
    for letter in words_dict.keys():
        occurrences_amount = len(words_dict[letter])
        amount_words_per_letter.append(f'{letter}: {occurrences_amount}' )
    print(f'{amount_words_per_letter}')
    return words_dict

def see_words(text_file):
    words_dict = count_words_occurrences(text_file)

    while True:
        letter = str(input('Digite a inicial da qual deseja ver as ocorrências ou digite "quit" a qualquer momento para sair do programa: '))

        if letter == 'quit':
            break

        if len(letter) == 1 and letter.isalpha():
            print(f'As palavras presentes no texto que se iniciam com a letra "{letter}" são: {words_dict[letter]}')

        else:
            print('Letra não encontrada.')

text_file = input('Escreva o nome do arquivo de texto que deseja ler caso ele esteja na mesma pasta deste programa ou o caminho para ele caso contrário: \n')
see_words(text_file)
