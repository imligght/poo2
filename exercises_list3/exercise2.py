def get_stop_words(stop_words_file):
    with open(stop_words_file, 'r') as file:
        stop_words = set([word.removesuffix('\n') for word in file.readlines()])
    return stop_words

def delete_stop_words(words_dict, stop_words):
    words_with_out_stop_words = {[word for word in words_dict if word not in  stop_words]}


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

    return words_dict

def show_words_amount(words_dict):
    amount_words_per_letter = []

    print('Esta é a quantidade de palavras iniciadas com cada letra:')
    for letter in words_dict.keys():
        occurrences_amount = len(words_dict[letter])
        amount_words_per_letter.append(f'{letter}: {occurrences_amount}' )
    print(f'{amount_words_per_letter}')

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

text_file = input('Escreva o nome do arquivo de texto que deseja ler caso ele esteja na mesma pasta deste programa ou o caminho para ele caso contrário:\n')
stop_words_file = input('Forneça o caminho do arquivo das "stop words":\n')
stopwords = get_stop_words(stop_words_file)
words = count_words_occurrences(text_file)
words_with_out_stop_words = delete_stop_words(words, stopwords)
print(show_words_amount(words_with_out_stop_words))
