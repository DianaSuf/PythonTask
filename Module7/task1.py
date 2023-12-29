# Ревью кода
students = {
1: {
'name': 'Bob',
'surname': 'Vazovski',
'age': 23,
'interests': ['biology, swimming']
},
2: {
'name': 'Rob',
'surname': 'Stepanov',
'age': 24,
'interests': ['math', 'computer games', 'running']
},
3: {
'name': 'Alexander',
'surname': 'Krug',
'age': 22,
'interests': ['languages', 'health food']
}
}

print(f'Список пар «ID студента — возраст»: {list(zip(students.keys(), [student["age"] for student in students.values()]))}')
print(f'Полный список интересов всех студентов: {set(interest for student in students.keys() for interest in students[student]["interests"])}')
print(f'Общая длина всех фамилий студентов: {sum(len(students[student]["surname"]) for student in students)}')