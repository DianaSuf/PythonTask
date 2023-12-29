# Студенты
class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

students = []
for i in range(10):
    name = input(f"Введите ФИО {i+1}-го студента: ")
    group = input(f"Введите номер группы {i+1}-го студента: ")
    grades = []
    for j in range(5):
        grade = int(input(f"Введите оценку {j+1}-го предмета для {i+1}-го студента: "))
        grades.append(grade)
    students.append(Student(name, group, grades))

students.sort(key=lambda x: x.average_grade())

print("Список студентов, отсортированный по возрастанию среднего балла:")
for student in students:
    print(f"{student.name}, {student.group}, средний балл: {student.average_grade()}")