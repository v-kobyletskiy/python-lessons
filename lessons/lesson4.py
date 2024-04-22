# Task 1
number = 1321
n1 = number // 1000
n2 = number // 100 % 10
n3 = number // 10 % 10
n4 = number % 10
print('Lucky ticket' if n1 + n2 == n3 + n4 else 'Ordinary ticket')

# Task 2 (143341, 7117)
digit = input('digit>>>')
i = 0
halfDigitSize = len(digit) / 2
while i < halfDigitSize:
    if digit[i] != digit[-i-1]:
        print('Not ideal digit')
        break
    i += 1
else:
    print('Ideal digit')

# Task 3
x = int(input('x>>>'))
y = int(input('y>>>'))
radius = 4
print('Point inside circle' if x ** 2 + y ** 2 <= radius ** 2 else 'Point outside circle')

# Task 4
for item in range(7, 100, 7):
    print(item)
print(list(range(7, 100, 7)))

# Task 5
summa = 0
for item in range(1, 100, 2):
    summa += item
print(summa)

# Task 6
digit_in_row = 5
limit = 200
count_rows = limit // digit_in_row
i = 0
while i < count_rows:
    x = list(range(digit_in_row * i + 1, digit_in_row * (i + 1) + 1))
    print(x)
    i += 1

# Task 7
n = int(input('n>>>'))
factorial = 1
i = 2
while i <= n:
    factorial *= i
    i += 1
print(factorial)

# Task 8
for i in range(1, 11):
    print(f'{i} x 5 = {i * 5}')

# Task 9
width = int(input('width>>>'))
height = int(input('height>>>'))
star = '*'
for i in range(height):
    if i == 0 or i == height - 1:
        print(star * width)
    else:
        x = []
        for j in range(width):
            x.append(star if j == 0 or j == width - 1 else ' ')
        print(''.join(x))

# Task 10
x = [0, 5, 2, 4, 7, 1, 3, 19]
odd_amount = 0
for i in range(len(x)):
    if x[i] % 2:
        odd_amount += 1
print(odd_amount)

# Task 11
import random
a = [random.randint(0, 10) for _ in range(4)]
b = a[:]
b.extend([item * 2 for item in a])
print(a)
print(b)

# Task 12
import random
salary = [random.randint(0, 100) for _ in range(12)]
year_income = 0
for i, item in enumerate(salary):
    year_income += item
print(f'salary: {salary}, average: {year_income / len(salary):.2f}')

# Task 13
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for i in range(len(matrix)):
    print(matrix[i])
matrix_sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix_sum += matrix[i][j]
print(matrix_sum)

# Task 14
a = [7, 2, 9, 4]
a_reversed = a[::-1]
print(a_reversed)
# a.reverse()
# print(a)

# Task 15
def isSimpleDigit(numeric):
    i = 2
    while i < numeric:
        if numeric % i == 0:
            break
        i += 1
    else:
        return True
    return False
x = []
for i in range(1, 100):
    if isSimpleDigit(i):
        x.append(i)
print(x)

# Task 16
width = int(input('width>>>'))
matrix = []
space_amount = 0
space_step = 2
for i in range(width):
    matrix.append([])
    for j in range(width):
        is_space_symbol = j < space_amount / 2 or j >= width - space_amount / 2
        matrix[i].append(' ' if is_space_symbol else '*')
    space_amount += (space_step if i < width / 2 - 1 else -space_step)
for i in range(width):
    print(''.join(matrix[i]))




















# a = [1,2,3]
# digit = int(input('digit>>>'))
# i = 2
# while i < digit:
#     if digit % i == 0:
#         print('Not prime')
#         break
#     i += 1
# else:
#     print('Prime')
#
# z = list('Hello')
# print(z)

# i = 1
# while i <= 5:
#     i += 1
#     if i == 2:
#         continue
#     print(i)
# else:
#     print('End')

# x = [1, 2, 3, 7, 7]
# y = [item + 10 for index, item in enumerate(x) if item % 2]
# print(y)

# x = [2, 3, 4, 5]
# y = ['bad', 'set', 'good', 'excellent']
# # res = list(zip(x, y))
# # print(res)
#
# for item_x, item_y in zip(x, y):
#     print(f'{item_x}-{item}')


# # Task 1
# ticket = input('ticket=')
# ticket = list(map(int, ticket))
# if len(ticket) % 2:
#     print('Error')
# else:
#     mid = len(ticket) // 2
#     res = 'Lucky' if sum(ticket[:mid]) == sum(ticket[mid:]) else 'Not Lucky'
#     print(res)

# # Task 2
# text = input('text=')
# res = 'Yes' if text == text[::-1] else 'No'
# print(res)

# # Task 3
# r = int(input('R='))
# x, y = int(input('x=')), int(input('y='))
# d = (x * x + y * y) ** 0.5
# if d < r:
#     print('In')
# elif d > r:
#     print('Out')
# else:
#     print('On')


# Task 4
# i = 0
# while i < 100:
#     print(i)
#     i += 7
#
# for i in range(0, 100, 7):
#     print(i)
#
# print(*range(0, 100, 7), sep='\n')
#
# # Task 5
# print(sum(range(1, 100, 2)), len(range(1, 100, 2))
# s = 0
# count = 0
# for i in range(1, 100, 2):
#     s += i
#     count += 1
# print(s, count)
#
# # Task 6
# for i in range(1, 201):
#     print(i, end=' ')
#     if i % 5 == 0:
#         print()
#
# # Task 7
# n = int(input('n='))
# if n < 0:
#     print('Error')
# else:
#     p = 1
#     for i in range(2, n + 1):
#         p *= i
#     print(p)
#
# # Task 8
# for i in range(1, 11):
#     print(f'5 x {i} = {5 * i}')
#
# # Task 9
# n, m = int(input('n=')), int(input('m='))
# res = f"{'*' * n}\n" + f"*{' ' * (n - 2)}*\n" * (m - 2) + f"{'*' * n}\n"
# print(res)
#
# # Task 10
# x = [112, 345, 5677, 77]
# s = 0
# for item in map(str, x):
#     s += sum(1 for digit in item if int(digit) % 2)
# print(s)
#
# # Task 11
# x = [1, 2, 3, 4]
# y = x[:] + [item * 2 for item in x]
# print(y)
#
# # Task 12
# import random
# salary = [random.randint(1, 10) for _ in range(12)]
# print(f'AVG: {sum(salary) / len(salary):.2f}')
#
# # Task 13
# x =[
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 12, 13, 14],
#     [11, 12, 13, 14],
# ]
#
# s = 0
# for row in x:
#     s += sum(row)
#     print(*row, sep='\t')
# print(f'Summa={s}')
#
# # Task 14
# x = [1, 2, 3, 4]
# print(x[::-1])
#
# # Task 15
# for n in range(2, 100):
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         print(n)
#
# # Task 16
# n = int(input('stars='))
# spaces = 0
# res = []
# for stars in range(n, 0, -2):
#     res.append(f"{' ' * spaces}{'*' * stars}")
#     spaces += 1
#
# res += res[-2::-1]
# print('\n'.join(res))

