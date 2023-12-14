# Task 1
# def transform_digits(digits, transformer):
#     transformed_digits = map(transformer, digits)
#     return sum(transformed_digits)
#
#
# digits_to_transform = [1, 2, 3]
# print(f'Sum of {[1, 2, 3]} increased by \'1\': {transform_digits(digits_to_transform, lambda item: item + 1)}')

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
