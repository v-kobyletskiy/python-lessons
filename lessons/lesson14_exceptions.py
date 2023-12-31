# Task 1
import time

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
            raise TypeError("Invalid type.")
        self.products.append(product)
        self.quantities.append(quantity)

    def remove_product(self, product: Product, quantity: int | float = 1):
        """
        Remove product from cart.
        """
        if not isinstance(product, Product) or not isinstance(quantity, (int, float)):
            raise TypeError("Invalid type.")
        if product not in self.products:
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
        cart.add_product(product_2)
        cart.add_product(product_3, 1.5)

        cart.remove_product(product_3, 0.5)
        print(cart)
    except InvalidPriceException as err:
        print(err)


# Task 2
class Discount:
    def discount(self):
        raise NotImplementedError
    def __str__(self):
        return f'Discount is {self.discount()}'


class RegularDiscount(Discount):
    def discount(self):
        return 0.01


class SilverDiscount(Discount):
    def discount(self):
        return 0.05


class GoldDiscount(Discount):
    def discount(self):
        return 0.1


class PlatinumDiscount(Discount):
    def discount(self):
        return 0.15

class InvalidDiscount(Discount):
    def discount(self):
        return 1.5

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} - {self.price}'

class DiscountException(Exception):
    def __init__(self, discount, message):
        self.discount = discount
        self.message = message
        super().__init__(message)
    def __str__(self):
        return f'{str(self.discount)}\n{self.message}'


class Customer:
    def __init__(self, name: str, discount: Discount):
        self.name = name
        if discount.discount() < 0 or discount.discount() > 1:
            raise DiscountException(discount, 'Invalid discount, not in range from 0 to 1')
        self.discount = discount


class Order:
    def __init__(self):
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int):
        self.products.append(product)
        self.quantities.append(quantity)

    def total_price(self, customer: Customer = None):
        discount = customer.discount.discount() if customer else 0
        total = 0
        for product, quantity in zip(self.products, self.quantities):
            total += product.price * quantity
        return total * (1 - discount)

    def __str__(self):
        return '\n'.join(map(str, self.products))


discounts = {
    'regular': RegularDiscount(),
    'silver': SilverDiscount(),
    'gold': GoldDiscount(),
    'platinum': PlatinumDiscount(),
    'invalid': InvalidDiscount(),
}

if __name__ == '__main__':
    print('Welcome to our shop!')
    print('Available discounts:')
    for discount in discounts:
        print(discount)
    while True:
        try:
            discount = input('Please choose discount: ')
            customer = Customer('John', discounts[discount])
            break
        except DiscountException as err:
            print(err)



    product1 = Product('banana', 100)
    product2 = Product('apple', 200)
    order = Order()
    order.add_product(product1, 2)
    order.add_product(product2, 1)

    print(order.total_price(customer))
