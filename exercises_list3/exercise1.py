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
        print(e)

    amount_per_letter = []

    for letter in words_dict.keys():
        occurrences_amount = len(words_dict[letter])
        amount_per_letter.append([f'{letter}: {occurrences_amount}' ])
    return amount_per_letter

text_file = 'article.txt'
print(count_words_occurrences(text_file))
