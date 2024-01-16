def simple(limit):
    digit = 1
    while digit < limit:
        if is_simple(digit):
            yield digit
        digit += 1
        print('After yield')


def is_simple(number):
    index = 2
    while index < number:
        if number % index == 0:
            break
        index += 1
    else:
        return True
    return False

def simple2(limit):
    for i in range(2, limit):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i

# simple_generator = simple2(100)
for x in simple2(100):
    print(x)