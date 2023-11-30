# Sets
# Task 1
list_to_check = [1, 7, 8, 9, 7]
unique_list_items = set(list_to_check)
if len(unique_list_items) == len(list_to_check):
    print('All elements is list is unique')
else:
    print('Not all elements in list is unique')

# Task 2
list_to_chjeck_2 = [1, 4, 5, 4, 5]
print(f'Count of unique elements: {len(set(list_to_chjeck_2))}')

# Task 3
dictionary = {
    'key1': 'val1',
    'key2': 'val1',
    'key3': 'val2',
    'key4': 'val3'
}
dict_values = tuple(dictionary.values())
uniques_values = set(dict_values)
unique_set = {val for val in uniques_values if dict_values.count(val) == 1}
print(unique_set)

# Task 4
friendships = {
    "user1": {"user2", "user3", "user4"},
    "user2": {"user1", "user3"},
    "user3": {"user1", "user2", "user4"},
    "user4": {"user1", "user3"}
}
user_1, user_2 = input('Please enter user1>>>'), input('Please enter user2>>>')
if user_1 in friendships and user_2 in friendships:
    print(set(friendships[user_1]) & set(friendships[user_2]))
else:
    print('Invalid user')

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
    for i in range(height):
        print('*' * width)
width_stars = 5
height_stars = 4
draw_stars(width_stars, height_stars)

# Task 3
from typing import List
def index(list: List[int], digit: int):
    if digit in list:
        return list.index(digit)
    else:
        return -1
print(index([1,2,3], 3))
print(index([1,2,3], 4))

# Task 4
def count_words(string: str) -> int:
    return len(string.split())
print(count_words('aaa bb c'))

# Task 5
def convert_int_to_string(digit: int) -> str:
    result = ''
    till_20_names = {
        '00': 'zero',
        '01': 'one',
        '02': 'two',
        '03': 'three',
        '04': 'four',
        '05': 'five',
        '06': 'six',
        '07': 'seven',
        '08': 'eight',
        '09': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen'
    }
    dozens_names = {
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
    }
    digit_till_100 = str(digit % 100)
    if digit_till_100 in till_20_names:
        result = till_20_names[str(digit_till_100)]
    else:
        unit = int(digit_till_100) % 10
        dozen = int(digit_till_100) - unit
        if dozen in dozens_names:
            result = dozens_names[dozen]
        if unit:
            result += f' {till_20_names[str(unit).zfill(2)]}'
    hundreds = digit // 100
    if hundreds:
        result = f'{till_20_names[str(hundreds).zfill(2)]} {'hundred' if hundreds == 1 else 'hundreds'} {result}'
    return result
def covert_float_to_string(digit: float) -> str:
    return f'{convert_int_to_string(int(digit//1))} dollars {convert_int_to_string(int(digit*100%100))} cents'

print(covert_float_to_string(123.34)) # one hundred twenty three dollars thirty four cents






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