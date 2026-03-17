from abc import ABC, abstractmethod
import math


# -------------------------
# Завдання 1
# -------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Employee.__init__(self, name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size


# тест
team_lead = TeamLead("Dmytro", 5000, "IT", "Python", 5)

print("Name:", team_lead.name)
print("Salary:", team_lead.salary)
print("Department:", team_lead.department)
print("Programming language:", team_lead.programming_language)
print("Team size:", team_lead.team_size)


# -------------------------
# Завдання 2
# -------------------------

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Figure):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


class Circle(Figure):

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))


# створення об'єктів
figures = [
    Rectangle(10, 5),
    Circle(7),
    Triangle(3, 4, 5)
]

# цикл
for fig in figures:
    print("Area:", fig.area())
    print("Perimeter:", fig.perimeter())
    print("------")