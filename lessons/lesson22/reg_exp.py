import re

# Task 1
result = re.findall(r'Rb+r', 'abc Rbbr def aRbbbr')
print(result)

# Task 2
# is_bank_card = re.match(r'^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}$', '1111-2222-3333-4444')
is_bank_card = re.match(r'^(\d{4}-){3}\d{4}$', '1111-2222-3333-4444')
print('Bank card' if is_bank_card else 'Not bank card')

# Task 3
def is_email(email):
    # return re.match(r'^[0-9A-Za-z][0-9A-Za-z_-]*@[A-Za-z]+\.[a-z]{2,3}$', email)
    return re.match(r'^[0-9A-Za-z](-?[0-9A-Za-z_])*@[a-zA-Z0-9](.[a-zA-Z0-9]+)*$', email)

print(is_email('text@gmail.com'))

# Task 4
def is_login(login):
    return re.match(r'^[0-9A-Za-z]{2,10}$', login)

print(is_login('ab'))
print(is_login('a'))
