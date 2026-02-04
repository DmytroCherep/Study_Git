# homework_06_4.py
# Calculate the sum of all EVEN numbers in a list

numbers = [1, 2, 3, 4, 5, 6, 10, 13, 18, 21, 24]

even_sum = 0

for num in numbers:
    if isinstance(num, int) and num % 2 == 0:
        even_sum += num

print("List of numbers:")
print(numbers)

print("\nSum of even numbers:")
print(even_sum)
