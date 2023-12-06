# Task 1
def isArifmetical(sequence):
    return sequence[2] == sequence[1] + getArifmeticalStep(sequence)
def getArifmeticalStep(sequence):
    return sequence[-1] - sequence[-2]
def getArifmeticalNext(sequence):
    return sequence[-1] + getArifmeticalStep(sequence)
def isGeometrical(sequence):
    return sequence[-2] == sequence[-3] * getGeometricalStep(sequence)
def getGeometricalStep(sequence):
    return sequence[-1] / sequence[-2]
def  getGeometricalNext(sequence):
    return sequence[-1] * getGeometricalStep(sequence)
def isSquared(sequence):
    square_root_last = sequence[-1] ** 0.5
    return sequence[-2] == int((square_root_last - 1) ** 2)
def getNextDegreeElement(sequence, degree):
    return (len(sequence) + 1) ** degree
def ifThirdDegree(sequence):
    for i in range(len(sequence)):
        if sequence[i] != (i + 1) ** 3:
            break
    else:
        return True
    return False


sequence = input('Please enter sequence>>>').replace(',', ' ').split()
sequence = tuple(map(int, sequence))
if isArifmetical(sequence):
    print(f'Arithmetical next element: {getArifmeticalNext(sequence)}')
elif isGeometrical(sequence):
    print(f'Geometrical next element: {getGeometricalNext(sequence)}')
elif isSquared(sequence):
    print(f'Squared next element: {getNextDegreeElement(sequence, 2)}')
elif ifThirdDegree(sequence):
    print(f'Third degree next element: {getNextDegreeElement(sequence, 3)}')
else:
    print('No regularity found')

# Task 2
def is_palindrome(digit: int) -> bool:
    return str(digit) == str(digit)[::-1]

palindrome_multipliers = ()
max_palindrome = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i * j) and i * j > max_palindrome:
            palindrome_multipliers = (i, j)
            max_palindrome = i * j
print(f'Palindrome: {max_palindrome} is result of multipliers {palindrome_multipliers}')

# def calc(*args, **kwargs):
#     for item in args:
#         if not isinstance(item, int | float):
#             raise TypeError()
#     if kwargs.get('operation') == '+':
#         print(sum(args))
#     # elif kwargs.operation == '*':
#         # print(numpy.prod(args))
#
#
# calc(1, 2, 3, operation='+')
