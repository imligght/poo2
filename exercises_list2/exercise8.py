ages = []
heights = []
for i in range(5):
    person_age = int(input('Insira sua idade: '))
    person_height = float(input('Insira sua altura: '))
    ages.append(person_age)
    heights.append(person_height)

print('Idades em ordem inversa: ', list(reversed(ages)))
print('Alturas em ordem inversa: ', list(reversed(heights)))
