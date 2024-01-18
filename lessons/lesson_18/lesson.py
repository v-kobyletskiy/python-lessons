# Task 1
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def __setattr__(self, key, value):
        if key == 'balance':
            raise AttributeError('You cant set balance directly')
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        raise AttributeError(f'property \'{item}\' doesn\'t exists')


bank_account = BankAccount(17)
print(bank_account.absent_prop)
print(bank_account.balance)
bank_account.balance = 47

# Task 2
class User:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    def __setattr__(self, key, value):
        if key in ('first_name', 'last_name'):
            raise AttributeError('You cant set \'first_name\' or \'last_name\' directly')
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return f'property \'{item}\' doesn\'t exists'

user = User('Ivan', 'Ivanov')
print(user.absent_prop)
user.first_name = 'Abc'

# Task 3
class Rectabgle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def __setattr__(self, key, value):
        if key in ['width', 'height']:
            raise AttributeError('You cant set \'width\' or \'height\' directly')
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return f'property \'{item}\' doesn\'t exists'

    def area(self):
        return self.width * self.height


rectangle = Rectabgle(2, 5)
print(f'Rectangle area: {rectangle.area()}')
print(rectangle.absent_prop)
rectangle.width = 5
