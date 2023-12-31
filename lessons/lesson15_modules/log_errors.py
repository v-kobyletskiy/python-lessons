# Task 1
import time
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('log.txt')
terminal_handler = logging.StreamHandler()

file_handler.setLevel(logging.WARNING)
terminal_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(terminal_handler)

class InvalidPriceException(Exception):
    def __init__(self, price, message):
        self.price = price
        self.message = message
        super().__init__(message)


class Product:
    """
    Product class.
    """
    def __init__(self, name: str, price: float | int):
        self.name = name
        if price <= 0:
            logger.error(f'Product {name} zero or negative price was attempted to set')
            raise InvalidPriceException(price, 'Zero or negative price was attempted to set')
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"


class Cart:
    """
    Cart class.
    """
    def __init__(self):
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int | float = 1):
        """
        Add product to cart.
        """
        if not isinstance(product, Product) or not isinstance(quantity, (int, float)):
            logger.debug(f'add_product invalid parameters {product} or {quantity}')
            raise TypeError("Invalid type.")
        self.products.append(product)
        self.quantities.append(quantity)

    def remove_product(self, product: Product, quantity: int | float = 1):
        """
        Remove product from cart.
        """
        if not isinstance(product, Product) or not isinstance(quantity, (int, float)):
            logger.debug(f'remove_product invalid parameters {product} or {quantity}')
            raise TypeError("Invalid type.")
        if product not in self.products:
            logger.warning(f'Product {product} not in cart')
            raise ValueError("Product not in cart.")

        index = self.products.index(product)
        if self.quantities[index] < quantity:
            raise ValueError("Not enough quantity.")
        self.quantities[index] -= quantity
        if self.quantities[index] == 0:
            del self.products[index]
            del self.quantities[index]
        return None

    def total(self):
        """
        Calculate total price.
        """
        return sum(product.price * quantity for product, quantity in zip(self.products, self.quantities))

    def __len__(self):
        return len(self.products)

    def __str__(self):
        res = f'{time.ctime()}: Items {len(self)}\n'
        for product, quantity in zip(self.products, self.quantities):
            res += f'{product.name} - {product.price} x {quantity} = {product.price * quantity} UAH\n'
        res += f'Total: {self.total()} UAH'
        return res


if __name__ == '__main__':
    try:
        product_1 = Product('Milk', 20)
        product_2 = Product('Bread', 10)
        product_3 = Product('Meat', 100)

        cart = Cart()
        cart.add_product(product_1, 2)
        # cart.add_product(product_2)
        cart.add_product(product_3, 1.5)

        cart.remove_product(product_2, 0.5)
        print(cart)
    except InvalidPriceException as err:
        print(err)

# import logging
#
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# terminal_handler = logging.StreamHandler()
# file_handler = logging.FileHandler('log.txt')
#
# terminal_handler.setLevel(logging.DEBUG)  # Записывать все сообщения уровня DEBUG и выше в терминал
# file_handler.setLevel(logging.WARNING)  # Записывать все сообщения уровня INFO и выше в файл
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# terminal_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)
#
# logger.addHandler(terminal_handler)
# logger.addHandler(file_handler)
#
#
# class StudentsLimitError(Exception):
#     def __init__(self, max_students, message='Too many students'):
#         self.max_students = max_students
#         self.message = message
#         super().__init__()
#
#     def __str__(self):
#         return f'Limit of students is {self.max_students}\n. {self.message}'
#
#
# class Student:
#
#     def __init__(self, name, date_of_birth, sex):
#         self.name = name
#         self.date_of_birth = date_of_birth
#         self.sex = sex
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# class Group:
#
#     def __init__(self, title, max_students=10):
#         self.title = title
#         self.max_students = max_students
#         self.__students = []
#
#     def add_student(self, student: Student):
#         if not isinstance(student, Student):
#             logger.debug(f'Wrong type {type(student)}')
#             raise TypeError('Not a Student')
#         if student in self.__students:
#             logger.debug(f'Student {student} already in group {self.title}')
#             raise ValueError('Student already in group')
#         if len(self.__students) == self.max_students:
#             logger.warning(f'Limit of students is {self.max_students}')
#             raise StudentsLimitError(self.max_students)
#
#         self.__students.append(student)
#         logger.warning(f'Student {student} added to group {self.title}')
#
#
# if __name__ == '__main__':
#     st_1 = Student('Ivan', '01/01/2000', 'M')
#     st_2 = Student('Anna', '01/02/2000', 'F')
#
#     st_3 = Student('Ivan1', '01/01/2000', 'M')
#     st_4 = Student('Anna1', '01/02/2000', 'F')
#
#     group = Group('Group1', 3)
#     try:
#         group.add_student(st_1)
#         group.add_student(st_1)
#         group.add_student('Petro')
#         group.add_student(st_2)
#         group.add_student(st_3)
#         group.add_student(st_4)
#     except Exception as e:
#         pass
