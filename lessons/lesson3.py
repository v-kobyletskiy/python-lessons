#Task 1
count_floors = 9
count_apartments_per_floor = 4
count_entrance = 4
apartments_amount = count_floors * count_apartments_per_floor * count_entrance
apartment_number = int(input('appartment number>>>'))
if apartment_number > apartments_amount or apartment_number <= 0:
    print('Such apartment is absent')
else:
    print(f'Entrance number: {(apartment_number - 1) // (count_floors * count_apartments_per_floor) + 1}')
    print(f'Floor number: {(apartment_number - 1) // count_apartments_per_floor % count_floors + 1}')
    print(f'Number apartment on the floor: {(apartment_number -1) % count_apartments_per_floor + 1}')

#Task 2
year = int(input('Please enter year>>>'))
if (year % 4 == 0 and year % 100 or year % 400 == 0):
    print(366)
else:
    print(365)

#Task 3
a, b, c = int(input('a>>>')), int(input('b>>>')), int(input('c>>>'))
if a + b > c and a + c > b and b + c > a:
    print('Triangle exists')
else:
    print('The triangle doesn\'t exists')

#Task 1
password = '1111'
user_entrance = input('Please enter password>>>')
if user_entrance == password:
    print('You guessed the password')
else:
    print('You have not guessed the password')

#Task 2
purchase_amount = int(input('Please enter purchase amount>>>'))
if purchase_amount >= 1000:
    purchase_amount *= 0.9
print(f'{purchase_amount:.2f}')

#Task 3
month_number = int(input('Please enter month number>>>'))
if month_number in (1, 3, 5, 7, 8, 10, 12):
    print(31)
elif month_number in (4, 6, 9, 11):
    print(30)
elif month_number == 2:
    year = int(input('Please enter year>>>'))
    print(28 if year % 4 else 29)
else:
    print('Month number is out of range')

#Task 4
rating = int(input('Please enter rating 1-5>>>'))
rating_labels = ['Відмінно', 'Добре', 'Задовільно', 'Погано', 'Жахливо']
if rating < 1 or rating > 5:
    print('Incorrect rating')
else:
    print(rating_labels[-rating])

#Task 5
weight = int(input('Please enter weight in kg>>>'))
height = float(input('Please enter height in meters'))
bmi = weight / height ** 2
print(f'BMI: {bmi}')

if bmi <= 18.4:
    print('Underweight')
elif bmi <= 24.9:
    print('Normal')
elif bmi <= 39.9:
    print('Overweight')
else:
    print('Obese')
