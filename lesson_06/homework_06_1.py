# homework_06_1.py
# Task: count unique characters in input string

user_input = input("Enter a string: ")

unique_chars = set(user_input)

if len(unique_chars) > 10:
    print(True)
else:
    print(False)
