# Task 1
user_entrance = input('Enter string>>>')
print(f'Count "b" symbol {user_entrance.count('b')}')

# Task 2
user_name = input('Please enter name>>>')
is_capital = user_name[0:1].isupper()
is_lower = user_name[1::].islower()
is_letters = user_name.isalpha()
if is_capital and is_lower and is_letters:
    print('Valid name')
else:
    print('Invalid name')

# Task 3
string = input('Please enter string>>>')
string_sum = 0
for item in string:
    string_sum += ord(item)
print(string_sum)

# Task 4
import math
for i in range(10):
    print(f'{math.pi:.{i + 2}f}')

# Task 5
string = input('Please enter string>>>')
words = string.split()
longest_word = ''
for i in range(len(words)):
    if len(words[i]) > len(longest_word):
        longest_word = words[i]
print(longest_word)



# text = input('text>>>')
# while '  ' in text:
#     text = text.replace('  ', ' ')
# print(text)

# x = [
#     '1 Bob Simson 19.58$ decorations',
#     '2 Mary 66.7$ food',
#     '3 Mary 98.91$ toys',
#     '4 Aleksa 72.29$ drinks',
# ]
# sum = 0
# for i, item in enumerate(x):
#     sum += float(item.split()[-2:-3:-1][0].replace('$', ''))
# print(sum)
