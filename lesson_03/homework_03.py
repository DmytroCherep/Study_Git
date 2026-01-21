# =========================
# Task 01–03 (Strings)
# =========================

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# (порахуємо і покажемо, скільки їх)
single_quote_count = alice_in_wonderland.count("'")
print(f"Task 02: У тексті {single_quote_count} символів одинарної лапки (').")

# task 03 == Виведіть змінну alice_in_wonderland на друк
print("\nTask 03: Текст Alice in Wonderland:\n")
print(alice_in_wonderland)


# =========================
# Task 04–10 (Math, 5 grade)
# =========================

# task 04
black_sea = 436_402
azov_sea = 37_800
total_seas = black_sea + azov_sea
print("\nTask 04:")
print(f"Площа Чорного моря: {black_sea} км²")
print(f"Площа Азовського моря: {azov_sea} км²")
print(f"Разом: {black_sea} + {azov_sea} = {total_seas} км²")


# task 05
# Є 3 склади: A, B, C
# A + B + C = 375291
# A + B = 250449
# B + C = 222950

total = 375_291
a_plus_b = 250_449
b_plus_c = 222_950

# Знайдемо C:
# (A+B+C) - (A+B) = C
c = total - a_plus_b

# Знайдемо B:
# (B+C) - C = B
b = b_plus_c - c

# Знайдемо A:
# (A+B) - B = A
a = a_plus_b - b

print("\nTask 05:")
print(f"Всього на 3 складах: {total} товарів")
print(f"На 1-му та 2-му разом: {a_plus_b} товарів")
print(f"На 2-му та 3-му разом: {b_plus_c} товарів")
print("Знаходимо по черзі:")
print(f"3-й склад: {total} - {a_plus_b} = {c}")
print(f"2-й склад: {b_plus_c} - {c} = {b}")
print(f"1-й склад: {a_plus_b} - {b} = {a}")
print(f"Відповідь: 1-й = {a}, 2-й = {b}, 3-й = {c}")


# task 06
# 1.5 року = 18 місяців
months = 18
payment_per_month = 1_179
computer_price = months * payment_per_month

print("\nTask 06:")
print(f"Півтора року = {months} місяців")
print(f"Щомісячний платіж: {payment_per_month} грн")
print(f"Вартість комп'ютера: {months} * {payment_per_month} = {computer_price} грн")


# task 07
print("\nTask 07:")
examples = [
    ("a) 8019 : 8", 8019, 8),
    ("b) 9907 : 9", 9907, 9),
    ("c) 2789 : 5", 2789, 5),
    ("d) 7248 : 6", 7248, 6),
    ("e) 7128 : 5", 7128, 5),
    ("f) 19224 : 9", 19224, 9),
]

for label, x, y in examples:
    remainder = x % y
    print(f"{label} -> остача = {x} % {y} = {remainder}")


# task 08
print("\nTask 08:")
pizza_big_qty, pizza_big_price = 4, 274
pizza_mid_qty, pizza_mid_price = 2, 218
juice_qty, juice_price = 4, 35
cake_qty, cake_price = 1, 350
water_qty, water_price = 3, 21

total_order = (
    pizza_big_qty * pizza_big_price +
    pizza_mid_qty * pizza_mid_price +
    juice_qty * juice_price +
    cake_qty * cake_price +
    water_qty * water_price
)

print(f"Піца велика: {pizza_big_qty} * {pizza_big_price} = {pizza_big_qty * pizza_big_price} грн")
print(f"Піца середня: {pizza_mid_qty} * {pizza_mid_price} = {pizza_mid_qty * pizza_mid_price} грн")
print(f"Сік: {juice_qty} * {juice_price} = {juice_qty * juice_price} грн")
print(f"Торт: {cake_qty} * {cake_price} = {cake_qty * cake_price} грн")
print(f"Вода: {water_qty} * {water_price} = {water_qty * water_price} грн")
print(f"Разом потрібно: {total_order} грн")


# task 09
print("\nTask 09:")
photos = 232
per_page = 8
# Скільки сторінок треба: ділення з округленням вгору
pages = (photos + per_page - 1) // per_page

print(f"Фотографій: {photos}")
print(f"На одній сторінці максимум: {per_page}")
print(f"Сторінок потрібно: ({photos} + {per_page} - 1) // {per_page} = {pages}")


# task 10
print("\nTask 10:")
distance_km = 1600
fuel_per_100km = 9
tank_capacity = 48

# 1) Скільки літрів потрібно:
fuel_needed = (distance_km / 100) * fuel_per_100km

# 2) Скільки разів заїхати на заправку, кожного разу повний бак:
# Скільки повних баків потрібно = округлення вгору (fuel_needed / tank_capacity)
refuels = int((fuel_needed + tank_capacity - 1) // tank_capacity)

print(f"Відстань: {distance_km} км")
print(f"На кожні 100 км потрібно: {fuel_per_100km} л")
print(f"Потрібно бензину: ({distance_km}/100) * {fuel_per_100km} = {fuel_needed} л")

print(f"Місткість баку: {tank_capacity} л")
print(f"Мінімум повних заправок: ceil({fuel_needed} / {tank_capacity}) = {refuels}")

