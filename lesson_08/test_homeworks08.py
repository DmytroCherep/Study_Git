from homeworks import (
    sum_two_numbers,
    average_of_list,
    reverse_string,
    longest_word,
    filter_cars
)


def test_sum_two_numbers_positive():
    assert sum_two_numbers(2, 3) == 5


def test_sum_two_numbers_negative():
    assert sum_two_numbers(-2, -3) == -5


def test_average_of_list_basic():
    assert average_of_list([1, 2, 3, 4]) == 2.5


def test_average_of_list_empty():
    assert average_of_list([]) == 0


def test_reverse_string_basic():
    assert reverse_string("hello") == "olleh"


def test_reverse_string_empty():
    assert reverse_string("") == ""


def test_longest_word_basic():
    assert longest_word(["cat", "elephant", "dog"]) == "elephant"


def test_longest_word_empty():
    assert longest_word([]) == ""


def test_filter_cars_returns_max_five():
    car_data = {
        'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
        'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
        'Honda': ('red', 2017, 1.6, 'sedan', 30000),
        'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
        'Kia': ('white', 2020, 2.0, 'sedan', 28000),
        'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
        'Volkswagen': ('brown', 2021, 1.6, 'hatchback', 28000),
    }
    search_criteria = (2017, 1.6, 36000)

    result = filter_cars(car_data, search_criteria)

    assert len(result) <= 5


def test_filter_cars_sorted_by_price():
    car_data = {
        'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
        'Honda': ('red', 2017, 1.6, 'sedan', 30000),
        'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
    }
    search_criteria = (2017, 1.6, 40000)

    result = filter_cars(car_data, search_criteria)

    assert result[0][0] == 'Toyota'
    assert result[1][0] == 'Honda'
    assert result[2][0] == 'Mazda'


def test_filter_cars_filters_correctly():
    car_data = {
        'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
        'OldCar': ('black', 2010, 2.0, 'sedan', 20000),
        'ExpensiveCar': ('white', 2021, 2.0, 'sedan', 50000),
    }
    search_criteria = (2017, 1.6, 30000)

    result = filter_cars(car_data, search_criteria)

    assert len(result) == 1
    assert result[0][0] == 'Toyota'