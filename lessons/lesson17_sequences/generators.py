# Task 3
def generate_geometrical(start, multiplier):
    current_item = start
    while True:
        yield current_item
        current_item *= multiplier

geometry_generator = generate_geometrical(1, 2)
print(next(geometry_generator))
print(next(geometry_generator))
print(next(geometry_generator))

# Task 4
def range_test(finish):
    index = 0
    while index < finish:
        yield index
        index += 1

for i in range_test(5):
    print(i)

# Task 5

def gen_simple_numbers(top_bound):
    index = 1
    while index < top_bound:
        if is_simple(index):
            yield index
        index += 1

def is_simple(number):
    index = 2
    while index < number:
        if number % index == 0:
            break
        index += 1
    else:
        return True
    return False

simple_numbers_gen = gen_simple_numbers(5)
print(next(simple_numbers_gen))
print(next(simple_numbers_gen))
print(next(simple_numbers_gen))
print(next(simple_numbers_gen))

# Task 6
cube_list = []
cube_generator = (i**3 for i in range(2, 5))
for digit_cube in cube_generator:
    cube_list.append(digit_cube)
print(cube_list)

# Task 7

def gen_fibonachi():
    previous = 1
    current = 1
    yield previous
    yield current
    while True:
        temp = current
        current += previous
        previous = temp
        yield current

fibonachi_generator = gen_fibonachi()
print(next(fibonachi_generator))
print(next(fibonachi_generator))
print(next(fibonachi_generator))
print(next(fibonachi_generator))
print(next(fibonachi_generator))

# Task 8
from datetime import datetime, timedelta

def generate_date(start, end):
    current_date = start
    while current_date < end:
        current_date += timedelta(days=1)
        yield current_date

date_generator = generate_date(datetime(2024, 1, 1), datetime(2024, 1, 3))
print(next(date_generator))
print(next(date_generator))
