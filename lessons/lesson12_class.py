# Task 1
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
class Card:
    """
    Class represents customer shopping's
    """
    def __init__(self):
        self.shoppings = []

    def add_shopping(self, product: Product, amount):
        if not isinstance(product, Product):
            raise ValueError('Not valid product in \'add_shopping\' first parameter')
        self.shoppings.append((product, amount))

    def cost_shoppings(self):
        return sum([shopping[0].price * shopping[1] for shopping in self.shoppings])

    def __str__(self):
        return f'Shopping\'s:\n{'\n'.join(map(lambda shopping: f'{shopping[0].name} - {shopping[1]}' +
                                                               f' {shopping[0].measure_units}', self.shoppings))}'

potato = Product('potato', 12.50, 'kg', 'Vegetable')
sidr = Product('sidr', 65.50, 'bottle', 'Low alcohol drink')
orange = Product('orange', 75.00, 'kg', 'Fruit')

ivan_shoppings = Card()
ivan_shoppings.add_shopping(potato, 1)
ivan_shoppings.add_shopping(sidr, 2)
ivan_shoppings.add_shopping(orange, 3)

print(f'{ivan_shoppings}')
print(f'Ivan\'s sum of shoppings is: ${ivan_shoppings.cost_shoppings()}')

# Task 2
class Dish:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    def __str__(self):
        return f'{self.name.title()} {self.price} {self.description}'

class MenuCategory:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes
    def __str__(self):
        return f'{self.name.title()}\n{'\n'.join(map(lambda dish: str(dish), self.dishes))}'


borsch = Dish('borsch', 78.00, 'beet soup')
lobio = Dish('lobio', 68.00, 'boiled red beans with greens and/or pomegranate seeds')
brusceta = Dish('brusceta', 55.00, 'traditional italian snack, fried bread with prosciutto')
stuffed_eggs = Dish('stuffed eggs', 48.00, 'boiled eggs with stuffing')
kusil = Dish('kusil', 25.00, 'a gelatinous dish or drink made from berry or fruit syrup')
ukler = Dish('ukler', 35.00, 'cake with cream')
main_dishes = MenuCategory('Main dishes', [borsch, lobio])
appetizers = MenuCategory('Appetizers', [brusceta, lobio])
desserts = MenuCategory('Desserts', [kusil, ukler])
menu = [main_dishes, appetizers, desserts]

for category in menu:
    print(f'{category}\n')
