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
    def __iadd__(self, other):
        self.dishes.append(other)
        return self


borsch = Dish('borsch', 78.00, 'beet soup')
lobio = Dish('lobio', 68.00, 'boiled red beans with greens and/or pomegranate seeds')
brusceta = Dish('brusceta', 55.00, 'traditional italian snack, fried bread with prosciutto')
stuffed_eggs = Dish('stuffed eggs', 48.00, 'boiled eggs with stuffing')
kusil = Dish('kusil', 25.00, 'a gelatinous dish or drink made from berry or fruit syrup')
ukler = Dish('ukler', 35.00, 'cake with cream')

main_dishes = MenuCategory('Main dishes', [lobio])
appetizers = MenuCategory('Appetizers', [brusceta, lobio])
desserts = MenuCategory('Desserts', [kusil, ukler])

main_dishes += borsch

menu = [main_dishes, appetizers, desserts]

for category in menu:
    print(f'{category}\n')
