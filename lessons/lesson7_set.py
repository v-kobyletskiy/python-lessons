# Sets
# Task 1
import random
list_digits = [random.randint(1, 10) for _ in range(5)]
res = 'Yes' if len(list_digits) == len(set(list_digits)) else 'No'
print(f'Is all unique: {res} {list_digits}')

# Task 2
list_to_check_2 = [1, 4, 5, 4, 5]
count_unique = 0
for item in list_to_check_2:
    if list_to_check_2.count(item) == 1:
        count_unique += 1
print(f'Count of unique elements: {count_unique}')

# Task 3
dict_3 = {i: random.randint(1, 10) for i in range(5)}
res = 'Has uniques values' if len(dict_3) == len(set(dict_3.values())) else 'No unique values in dict'
print(res)

# Task 4
friendships = {
    "user1": {"user2", "user3", "user4"},
    "user2": {"user1", "user3"},
    "user3": {"user1", "user2", "user4"},
    "user4": {"user1", "user3"}
}
user1, user2 = input('Please enter user1>>>').lower().strip(), input('Please enter user2>>>').lower().strip()
print(friendships.get(user1, set()) & friendships.get(user2, set()))

# Task 5
string_1, string_2 = input('Please enter string1>>>'), input('Please enter string 2>>>')
joint_words = set(string_1.split()) & set(string_2.split())
print(max(joint_words, key=len))

# Functions
# Task 1
def function_1(digit1: int | float, digit2: int | float, prefix: str) -> str:
    return f'{prefix}: {digit1 + digit2}'
print(function_1(2,3, 'Sum of 2 and 3'))

# Task 2
def draw_stars(width, height):
    star_sign = '*'
    space_sign = ' '
    return f'{star_sign * width} \n' + f'{star_sign}{space_sign*(width-2)}{star_sign}\n' * (height - 2) + f'{star_sign * width} \n'
width_stars = 5
height_stars = 4
print(draw_stars(width_stars, height_stars))

# Task 3
from typing import List
def index(list: List[int], digit: int):
    for index, item in enumerate(list):
        if item == digit:
            return index
    return -1
print(index([1,2,3], 3))
print(index([1,2,3], 4))

# Task 4
def count_words(string: str) -> int:
    return len(string.split())
print(count_words('aaa bb c'))

# Task 5
import num2words
dollars, cents = input('money $=').split('.')
print(f'{num2words.num2words(dollars)} dollars {num2words.num2words(cents)} cents')


# def convert_int_to_string(digit: int) -> str:
#     result = ''
#     till_20_names = {
#         '00': 'zero',
#         '01': 'one',
#         '02': 'two',
#         '03': 'three',
#         '04': 'four',
#         '05': 'five',
#         '06': 'six',
#         '07': 'seven',
#         '08': 'eight',
#         '09': 'nine',
#         '10': 'ten',
#         '11': 'eleven',
#         '12': 'twelve',
#         '13': 'thirteen',
#         '14': 'fourteen',
#         '15': 'fifteen',
#         '16': 'sixteen',
#         '17': 'seventeen',
#         '18': 'eighteen',
#         '19': 'nineteen'
#     }
#     dozens_names = {
#         20: 'twenty',
#         30: 'thirty',
#         40: 'forty',
#         50: 'fifty',
#         60: 'sixty',
#         70: 'seventy',
#         80: 'eighty',
#         90: 'ninety',
#     }
#     digit_till_100 = str(digit % 100)
#     if digit_till_100 in till_20_names:
#         result = till_20_names[str(digit_till_100)]
#     else:
#         unit = int(digit_till_100) % 10
#         dozen = int(digit_till_100) - unit
#         if dozen in dozens_names:
#             result = dozens_names[dozen]
#         if unit:
#             result += f' {till_20_names[str(unit).zfill(2)]}'
#     hundreds = digit // 100
#     if hundreds:
#         result = f'{till_20_names[str(hundreds).zfill(2)]} {'hundred' if hundreds == 1 else 'hundreds'} {result}'
#     return result
# def covert_float_to_string(digit: float) -> str:
#     return f'{convert_int_to_string(int(digit//1))} dollars {convert_int_to_string(int(digit*100%100))} cents'
#
# print(covert_float_to_string(123.34)) # one hundred twenty three dollars thirty four cents






# def add(a: int | float, b: int | float, c: int | float = 10) -> int | float:
#     """
#     Return sum of three numbers.
#     :param a: march salary
#     :param b: november salary
#     :param c: december salary
#     :return:
#     """
#     if not isinstance(a, int | float):
#         raise TypeError('a must be int or float')
#     if not isinstance(b, int | float):
#         raise TypeError('b must be int or float')
#     if not isinstance(c, int | float):
#         raise TypeError('c must be int or float')
#     res = a+b+c
#     return res
#
#
# add(10, 15, 16)

# def func_name(a, b=None):
#     if not b:
#         b = []
#     b.append(a)
#     return b
#
#
# func_name(1)
# sentence1_words = set(input('First sentence>>>').split())
# sentence2_words = set(input('Second sentence>>>').split())
# print(sentence1_words & sentence2_words)