class Product:
    """
    Class represents product instance
    """
    def __init__(self, name, price, measure_units, description):
        self.name = name
        self.price = price
        self.measure_units = measure_units
        self.description = description

    def __str__(self):
        return f'Name: {self.name} price: {self.price} description: {self.description}'

class CartIterator:
    def __init__(self, shoppings):
        self.__index = 0
        self.__shoppings = shoppings
    def __iter(self):
        return self
    def __next__(self):
        if self.__index < len(self.__shoppings):
            product = self.__shoppings[self.__index]
            self.__index += 1
            return product
        raise StopIteration


class Cart:
    """
    Class represents customer shopping's
    """
    def __init__(self):
        self.shoppings = []

    def __iadd__(self, other):
        if not isinstance(other, Cart):
            return NotImplemented
        for shopping in other.shoppings:
            self.add_shopping(shopping[0], shopping[1])
        return self

    def add_shopping(self, product: Product, amount):
        if not isinstance(product, Product):
            raise ValueError('Not valid product in \'add_shopping\' first parameter')
        self.shoppings.append((product, amount))

    def cost_shoppings(self):
        return sum([shopping[0].price * shopping[1] for shopping in self.shoppings])

    def __str__(self):
        return f'Shopping\'s:\n{'\n'.join(map(lambda shopping: f'{shopping[0].name} - {shopping[1]}' +
                                                               f' {shopping[0].measure_units}', self.shoppings))}'
    def __iter__(self):
        return CartIterator(self.shoppings)


potato = Product('potato', 12.50, 'kg', 'Vegetable')
sidr = Product('sidr', 65.50, 'bottle', 'Low alcohol drink')
orange = Product('orange', 75.00, 'kg', 'Fruit')

ivan_shoppings = Cart()
ivan_shoppings.add_shopping(potato, 1)
ivan_shoppings.add_shopping(sidr, 2)
ivan_shoppings.add_shopping(orange, 3)

for shopping in ivan_shoppings:
    print(f'{shopping[0]} : {shopping[1]}')

print(f'{ivan_shoppings}')
# print(f'Ivan\'s sum of shoppings is: ${ivan_shoppings.cost_shoppings()}')