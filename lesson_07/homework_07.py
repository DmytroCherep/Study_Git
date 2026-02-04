# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
"""

def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier
        if result > 25:
            break
        print(f"{number}x{multiplier}={result}")
        multiplier += 1


multiplication_table(3)


# task 2
""" Написати функцію, яка обчислює суму двох чисел. """

def sum_two_numbers(a, b):
    return a + b


# task 3
""" Написати функцію, яка розрахує середнє арифметичне списку чисел. """

def average_of_list(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# task 4
""" Написати функцію, яка приймає рядок та повертає його у зворотному порядку. """

def reverse_string(text):
    return text[::-1]


# task 5
""" Написати функцію, яка приймає список слів та повертає найдовше слово у списку. """

def longest_word(words):
    if not words:
        return ""
    return max(words, key=len)


# task 6
""" Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо ні.
"""

def find_substring(str1, str2):
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # -1


# task 7,8,9,10
""" Перетворення 4 попередніх задач у функції:
- sum_two_numbers
- average_of_list
- reverse_string
- longest_word
"""
def sum_two_numbers(a, b):
    return a + b

def average_of_list(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def reverse_string(text):
    return text[::-1]

def longest_word(words):
    if not words:
        return ""
    return max(words, key=len)

