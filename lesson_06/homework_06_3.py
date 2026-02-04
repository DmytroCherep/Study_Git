# homework_06_3.py
# Create a new list containing only string elements from the original list

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst2 = []

for item in lst1:
    if isinstance(item, str):
        lst2.append(item)

print("Original list:")
print(lst1)

print("\nList with only strings:")
print(lst2)
