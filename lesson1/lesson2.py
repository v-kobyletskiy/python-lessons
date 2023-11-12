def print_bool(message):
    return not print(message)
# Task 1
x = int(input('Please enter digit>>>'))
x < 0 and print(f'Negative number: {x}')

# Task 2
x = int(input('Please enter digit>>>'))
(x < 20 and print_bool('Digit is less then 20')) or print_bool('Digit is equal or greater that 20')

# Task 3
x = int(input('Please enter digit>>>'))
(x and print_bool('Digit isn\'t zero')) or print_bool('Digit is zero')

# Task 4
x = int(input('Please enter digit>>>'))
(x % 2 and print_bool('It is odd number')) or print_bool('It is even number')

#Task 5
x, y, z = int(input('Please enter digit>>>')), int(input('Please enter digit>>>')), int(input('Please enter digit>>>'))
x > y and x > z and print_bool('First digit is the greatest') or \
y > x and y > z and print_bool('Second digit is the greatest') or \
z > x and z > y and print_bool('Third digit is the greatest')

# Task 1
answer = input('Do you have driver\'s license?')
answer == 'yes' and print_bool('You can drive a car')
answer == 'no' and print_bool('You can\'t drive a car')

# Task 2
age = int(input('What is your age?'))
(age >= 18 and print_bool('You can get driver\'s license')) or print_bool('You can\'t get driver\'s license')

# Task 3
x = int(input('Please enter digit>>>'))
(x >= 0 and not x % 2 and print_bool('Digit is positive and even')) or print_bool('Digit doesn\'t meet the criteria')

# Task 4
x = int(input('Please enter digit>>>'))
(not x % 3 and x % 5 and print_bool('The number fits')) or print_bool('The number doesen\'t fits')
