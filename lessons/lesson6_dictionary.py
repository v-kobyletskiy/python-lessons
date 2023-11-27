# Task 1
text = input('Please enter text>>>')
words = text.split()
res = {}
for word in words:
    if word not in res:
        res[word] = text.count(word)
print(res)

# Task 2
translations = {
    'hello': 'привіт',
    'goodbye': 'до побачення',
    'cat': 'кіт',
    'dog': 'собака'
}
eng = input('Please enter english word>>>')
if eng in translations:
    print(translations[eng])
else:
    print('No translation')

# Task 3
phones = {}
while True:
    user_selection = int(input('''Please enter your choice>>>
1 - add contact
2 - remove contact
3 - get phone by name
4 - exit
'''))
    if user_selection == 1:
        name, phone = input('Name>>>'), input('Number')
        phones[name] = phone
        print(phones)
    elif user_selection == 2:
        name = input('Please enter name to delete>>>')
        if name in phones:
            del phones[name]
    elif user_selection == 3:
        name = input('Please enter name to get phone>>>')
        print(phones[name]) if name in phones else print('No such contact')
    else:
        break

# Task 4
exchange_rate = {
    '$': 35.98,
    '€': 39.39
}
user_input = input('Please enter currency (20.15$ or 15€)>>>')
currency = user_input[-1]
if currency in exchange_rate:
    print(f'Amount in hrivnas: {float(user_input[0:-1]) * exchange_rate[currency]:.2f}')
else:
    print('No such currency')






# days = {
#     1: 'monday',
#     2: 'tuesday',
#     3: 'wednesday',
#     4: 'thursday',
#     5: 'friday',
#     6: 'saturday',
#     0: 'sunday'
# }
#
# day = int(input('Day>>>'))
# print(days.get(day % 7))

# import string
#
# text = input('text=')
#
# for item in string.punctuation:
#     text = text.replace(item, ' ')
# # print(text.split())
# words = text.split()
# for i in range(len(words)):
#     if text.count(words[i]) == 1:
#         print(words[i])