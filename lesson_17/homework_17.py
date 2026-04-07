# -------------------------
# ГЕНЕРАТОРИ
# -------------------------

def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i


def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


# -------------------------
# ІТЕРАТОРИ
# -------------------------

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            num = self.current
            self.current += 1
            if num % 2 == 0:
                return num
        raise StopIteration


# -------------------------
# ДЕКОРАТОРИ
# -------------------------

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception caught: {e}")
            return None
    return wrapper


# -------------------------
# ТЕСТИ (приклад використання)
# -------------------------

if __name__ == "__main__":

    print("Generators:")
    print(list(even_numbers(10)))
    print(list(fibonacci(20)))

    print("\nReverse Iterator:")
    for item in ReverseIterator([1, 2, 3, 4]):
        print(item)

    print("\nEven Iterator:")
    for item in EvenIterator(10):
        print(item)

    print("\nDecorators:")

    @log_decorator
    def add(a, b):
        return a + b

    @exception_handler
    def divide(a, b):
        return a / b

    add(2, 3)
    divide(10, 2)
    divide(10, 0)