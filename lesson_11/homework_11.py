def sum_of_numbers_in_string(s):
    try:
        # розділяємо по комі
        numbers = s.split(',')
        # перетворюємо всі елементи у int
        total = sum(int(num) for num in numbers)
        return total
    except ValueError:
        return "Не можу це зробити!"


# список прикладу
my_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

# цикл обробки
for item in my_list:
    print(sum_of_numbers_in_string(item))