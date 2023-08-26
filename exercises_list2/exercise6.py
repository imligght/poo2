import random

student1 = []
student2 = []
student3 = []
student4 = []
students = [
    student1,
    student2,
    student3,
    student4
    ]
for student in students:
    for i in range(4):
        student.append(random.randint(0, 10))

for student in students:
    print(student)

count = 0
for student in students:
    count += 1
    average = sum(student) / len(student)
    print(f'A média do aluno {count} é: {average}')
