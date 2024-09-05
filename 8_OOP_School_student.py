class Student:
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight

class SchoolClass:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def calculate_average(self):
        total_age = 0
        total_height = 0
        total_weight = 0
        for student in self.students:
            total_age += student.age
            total_height += student.height
            total_weight += student.weight
        avg_age = total_age / len(self.students)
        avg_height = total_height / len(self.students)
        avg_weight = total_weight / len(self.students)
        return avg_age, avg_height, avg_weight

class_a = SchoolClass('A')
class_b = SchoolClass('B')

# Input for Class A
n = int(input())
for _ in range(n):
    age, height, weight = map(int, input().split())
    student = Student(age, height, weight)
    class_a.add_student(student)

# Input for Class B
m = int(input())
for _ in range(m):
    age, height, weight = map(int, input().split())
    student = Student(age, height, weight)
    class_b.add_student(student)

avg_age_a, avg_height_a, avg_weight_a = class_a.calculate_average()
avg_age_b, avg_height_b, avg_weight_b = class_b.calculate_average()

if avg_height_a > avg_height_b:
    print(f'{avg_age_a:.1f}\n{avg_height_a:.1f}\n{avg_weight_a:.1f}\nA')
elif avg_height_b > avg_height_a:
    print(f'{avg_age_b:.1f}\n{avg_height_b:.1f}\n{avg_weight_b:.1f}\nB')
else:
    if avg_weight_a < avg_weight_b:
        print(f'{avg_age_a:.1f}\n{avg_height_a:.1f}\n{avg_weight_a:.1f}\nA')
    elif avg_weight_b < avg_weight_a:
        print(f'{avg_age_b:.1f}\n{avg_height_b:.1f}\n{avg_weight_b:.1f}\nB')
    else:
        print('Same')