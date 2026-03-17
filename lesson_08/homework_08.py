# homework_08.py

class Student:

    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_grade):
        self.average_grade = new_grade

    def display_info(self):
        print("Student information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Average grade: {self.average_grade}")


# створюємо об'єкт студента
student1 = Student("Dmytro", "Cherep", 30, 85)

# виводимо інформацію
student1.display_info()

# змінюємо середній бал
student1.change_average_grade(92)

print("\nAfter grade change:")

# знову виводимо інформацію
student1.display_info()