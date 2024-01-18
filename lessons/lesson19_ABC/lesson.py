# Task 1
import math
class Shape:
    def square(self):
        return NotImplementedError

    def perimeter(self):
        return NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.__radius__ = radius

    def square(self):
        return math.pi * self.__radius__ ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius__

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width__ = width
        self.__height__ = height

    def square(self):
        return self.__width__ * self.__height__

    def perimeter(self):
        return 2 * (self.__width__ + self.__height__)

class Triangle(Shape):
    def __init__(self, a_side, b_side, c_side):
        self.__a_side = a_side
        self.__b_side = b_side
        self.__c_side = c_side

    def square(self):
        return self.__a_side * self.__b_side / 2

    def perimeter(self):
        return self.__a_side + self.__b_side + self.__c_side


if __name__ == '__main__':
    circle = Circle(2)
    rectangle = Rectangle(2, 4)
    triangle = Triangle(1, 2, 3)
    print(f'Circle square: {circle.square():.2f} perimeter {circle.perimeter():.2f}')
    print(f'Rectangle square: {rectangle.square():.2f} perimeter {rectangle.perimeter():.2f}')
    print(f'Triangle square: {triangle.square():.2f} perimeter {triangle.perimeter():.2f}')

# Task 2
class PaymentMeans:
    def make_pay(self):
        return NotImplementedError

class CreditCard(PaymentMeans):
    def make_pay(self):
        return 'Pay using credit card'

class BankTransfer(PaymentMeans):
    def make_pay(self):
        return 'Bank transfer'

class ElectronicWallet(PaymentMeans):
    def make_pay(self):
        return 'Electronic Wallet'

class PayProcessor:
    def __init__(self, payment_way: PaymentMeans):
        self.__payment_way = payment_way

    def pay(self):
        return self.__payment_way.make_pay()

    def set_payment_way(self, payment_way: PaymentMeans):
        self.__payment_way = payment_way

if __name__ == '__main__':
    credit_card = CreditCard()
    bank_transfer = BankTransfer()
    electronic_wallet = ElectronicWallet()
    pay_processor = PayProcessor(credit_card)
    print(pay_processor.pay())
    pay_processor.set_payment_way(bank_transfer)
    print(pay_processor.pay())
    pay_processor.set_payment_way(electronic_wallet)
    print(pay_processor.pay())
