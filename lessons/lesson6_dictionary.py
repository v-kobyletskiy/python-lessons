# Task 1
text = input('Please enter text>>>')
words = text.split()
res = {}
for word in words:
    if word not in res:
        res[word] = text.count(word)
print(res)
# or res = {word: text.count(word) for word in words}

# Task 2
translations = {
    'hello': 'привіт',
    'goodbye': 'до побачення',
    'cat': 'кіт',
    'dog': 'собака'
}
reverse_translation = {value: key for key, value in translations.items()}
user_word = input('Please enter english word>>>').strip().lower()
if user_word in translations:
    print(translations[user_word])
elif user_word in reverse_translation:
    print(reverse_translation.get(user_word, 'No translation'))


# Task 3
phones = {}
while user_selection := int(input('''Please enter your choice>>>
1 - add contact
2 - remove contact
3 - get phone by name
4 - exit
''')) != 4:

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

# Task 1
text = input('text=').split()
words = {word: text.count(word) for word in text}

print(words)

for word in text:
    if word not in words:
        words[word] = text.count(word)

print(words)

# Task 2
translations = {
     'hello': 'привет',
     'goodbye': 'до свидания',
     'cat': 'кот',
     'dog': 'собака'
}

translations_reverse = {value: key for key, value in translations.items()}

word = input('word=').strip().lower()
if word in translations:
    print(translations[word])
else:
    print(translations_reverse.get(word, 'No translation'))
    keys, values = tuple(translations.keys()), tuple(translations.values())
    if word in values:
        value_index = values.index(word)
        print(keys[value_index])
    else:
        print('No translation')

# Task 3
contacts = {}
prompt = """
1 - add contact\n
2 - rename contact\n
3 - del contact\n
4 - get contact\n
5 - exit\n
"""

while (ans := input(prompt)) != '5':
    if ans == 1:
        name = input('name>>>')
        if name not in contacts:
            phone = input('phone>>>')
            contacts[name] = phone
        else:
            print('Already exists')
    elif ans == 2:
        ...
    elif ans == 3:
        ...
    elif ans == 4:
        ...
    else:
        print('Error. Try again!')

# Task 4
exchange = {
    'USD': {
        'purchase': 37,
        'sale': 38,
    },
    'EUR': {
        'purchase': 41,
        'sale': 42,
    }
}

currency = input('Currency = ').upper()
operation = input('Operation = ').lower()
money = float(input('money = '))

current_currency = exchange.get(currency)
if current_currency:
    res = money * current_currency['purchase'] if operation == 'purchase' else money / current_currency['sale']
    print(f'{res:.2f}')
else:
    print('Error')
