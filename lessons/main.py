# First task
name = input('Please enter your name:')
print(f'Hello {name}!')

#Second task
firstDigit = int(input('Enter first digit'))
secondDigit = int(input('Enter second digit'))
thirdDigit = int(input('Enter third digit'))
fourthDigit = int(input('Enter fourth digit'))
fifthDigit = int(input('Enter fifth digit'))
print(f'min value: {min(firstDigit, secondDigit, thirdDigit, fourthDigit, fifthDigit)}')
print(f'max value: {max(firstDigit, secondDigit, thirdDigit, fourthDigit, fifthDigit)}')
print(f'average: {(firstDigit + secondDigit + thirdDigit + fourthDigit + fifthDigit)/5}')

#Third task
x = int(input('Enter first operand'))
y = int(input('Enter second operand'))
print(f'x + y: {x + y}')
print(f'x - y: {x - y}')
print(f'x * y: {x * y}')
print(f'x / y: {x / y}')
print(f'x // y: {x // y}')

#Fourth task
PI = 3.1415
circleRadius = int(input('Enter circle radius'))
print(f'Diametr: {circleRadius * 2}')
print(f'Circle length: {2 * PI * circleRadius}')
print('Circle square', PI * (circleRadius ** 2))

#Fifth task
startAmount = 1000
percentIncome = 0.1
print(f'Amount of money in 10 years: {startAmount * (1 + percentIncome) ** 10}')
print(f'Amount of money in 20 years: {startAmount * (1 + percentIncome) ** 20}')
print(f'Amount of money in 30 years: {startAmount * (1 + percentIncome) ** 30}')

#Sixth task
dollarExchangeRate = 37.7
dollarsAmount = int(input('Please enter dollars amount: '))
print(f'Amount dollars in hrivnas: {dollarsAmount * dollarExchangeRate}')

#Seventh task
threeDigitNumber = int(input('Please enter three digit number'))
print(threeDigitNumber // 100)
print(threeDigitNumber // 10 % 10)
print(threeDigitNumber % 10)