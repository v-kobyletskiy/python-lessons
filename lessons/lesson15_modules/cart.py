import time
from product import Product

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
