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


def filter_cars(car_data, search_criteria):
    min_year, min_engine, max_price = search_criteria
    filtered_cars = []

    for brand, data in car_data.items():
        color, year, engine_volume, car_type, price = data

        if year >= min_year and engine_volume >= min_engine and price <= max_price:
            filtered_cars.append((brand, color, year, engine_volume, car_type, price))

    filtered_cars.sort(key=lambda car: car[-1])
    return filtered_cars[:5]