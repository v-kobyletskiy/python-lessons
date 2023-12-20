# Task 1
def transform_digits(digits, transformer):
    transformed_digits = map(transformer, digits)
    return sum(transformed_digits)


digits_to_transform = [1, 2, 3]
print(f'Sum of {[1, 2, 3]} increased by \'1\': {transform_digits(digits_to_transform, lambda item: item + 1)}')

# Task 2
def read_cache(file_path):
    cache = dict()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            number, fibonacci = line.split()[0], line.split()[1]
            cache[number] = fibonacci
    return cache
def save_cache(file_path, cache):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(map(lambda item: f'{item[0]} {item[1]}\n', cache.items()))
def factorial_decorator(func):
    cache = read_cache('./data/lesson11_1.txt')
    def wrapper(*args, **kwargs):
        cache_key = str(args + tuple(kwargs.items()))
        if cache_key not in cache:
            cache[cache_key] = func(*args, **kwargs)
            save_cache('./data/lesson11_1.txt', cache)
        return cache[cache_key]
    return wrapper
@factorial_decorator
def count_fibonacci(number):
    if number < 2:
        return 1
    return count_fibonacci(number - 1) + count_fibonacci(number - 2)

print(count_fibonacci(5))
print(count_fibonacci(4))

# Task 3
import time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'Time function\'{func.__name__}\' evaluation: {end - start:.2f} seconds')
        return res

    return wrapper

@measure_time
def test_function():
    time.sleep(2)

test_function()

# Task 4
def limit_calls(max_calls):
    def decorator(func):
        calls_counter = 0
        def wrapper(*args, **kwargs):
            nonlocal calls_counter
            if calls_counter >= max_calls:
                # print(f'Exceeds call function \'{func.__name__}\' limit')
                return None
            else:
                calls_counter += 1
                return func(*args, **kwargs)

        return wrapper
    return decorator
@limit_calls(2)
def limit_calls_function():
    print('Call limit_calls_function')

limit_calls_function()
limit_calls_function()
limit_calls_function()

# Task 5
def cache_result(func):
    def wrapper(*args, **kwargs):
        cache_key = args
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]

    wrapper.cache = dict()
    return wrapper

@cache_result
def fibonacci(number):
    if number <= 1:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(5))
print(fibonacci(5))

# Closure
def outer_function(x):
    # Локальна змінна у зовнішній функції
    outer_variable = x

    # Внутрішня функція (замикання)
    def inner_function(y):
        # Має доступ до локальної змінної зовнішньої функції
        result = outer_variable + y
        return result

    # Повертає внутрішню функцію (замикання)
    return inner_function

# Створення замикання
closure_instance = outer_function(10)

# Виклик замикання
result_value = closure_instance(5)

print(result_value)  # Виведе: 15
