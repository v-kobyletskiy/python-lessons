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
#     sum += float(item.split()[-2].replace('$', ''))
# print(sum)


# # Task 1
# text = input('text=').lower()
# print(text.count('b'))
#
# # Task 2
# name = input('name>>>')
# if len(name) >= 2 and name.replace(' ', '').isalpha() and name.istitle():
#     print('Valid')
# else:
#     print('Error')
#
# # Task 3
# text = input('text=')
# res = sum(map(ord, text))
# print(res)
#
# # Task 4
# import math
#
# for i in range(2, 12):
#     print(f'{math.pi:.{i}f}')
#
# # Task 5
# text = input('text=').split()
# print(max(text, key=len))
#
# # Task 6
# text = input('text=')
# for i in range(1, len(text) + 1):
#     pattern = text[:i]
#     if len(pattern) * text.count(pattern) == len(text):
#         print(pattern)
#         break
#
# # Task 7
# html = """
# <ul class="menu" role="tree">
#
#     <li class="python-meta current_item selectedcurrent_branch selected">
#         <a href="/" title="The Python Programming Language" class="current_item selectedcurrent_branch selected">Python</a>
#     </li>
#
#     <li class="psf-meta ">
#         <a href="https://www.python.org/psf/" title="The Python Software Foundation" >PSF</a>
#     </li>
#
#     <li class="docs-meta ">
#         <a href="https://docs.python.org" title="Python Documentation" >Docs</a>
#     </li>
#
#     <li class="pypi-meta ">
#         <a href="https://pypi.org/" title="Python Package Index" >PyPI</a>
#     </li>
#
#     <li class="jobs-meta ">
#         <a href="/jobs/" title="Python Job Board" >Jobs</a>
#     </li>
#
#     <li class="shop-meta ">
#         <a href="/community-landing/"  >Community</a>
#     </li>
#
# </ul>
#
# """
#
# while '<' in html:
#     l_index = html.find('<')
#     r_index = html.find('>')
#     html = html.replace(html[l_index: r_index + 1], '')
#
# print(html)
