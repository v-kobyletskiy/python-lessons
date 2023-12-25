from abc import ABC, abstractmethod
class Discount(ABC):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount
    @abstractmethod
    def discount(self):
        raise NotImplementedError('subclass must implement \'discount\' method')

class RegularDiscount(Discount):
    def __init__(self, discount_amount):
        super().__init__(discount_amount)
    def discount(self):
        return self.discount_amount

class SilverDiscount(Discount):
    def discount(self):
        return self.discount_amount + 5

class GoldDiscount(Discount):
    def discount(self):
        return self.discount_amount + 15

class Client:
    def __init__(self, name, discount: Discount):
        self.name = name
        self.discount = discount
    def get_total_price(self, order):
        return sum(order) * (1 - self.discount.discount() / 100)

def main():
    today_discount = 10
    client_regular = Client('Ivan', RegularDiscount(today_discount))
    print(f'Regular client: {client_regular.get_total_price([10, 15, 20]):.2f}')
    silver_client = Client('Ihor', SilverDiscount(today_discount))
    print(f'Silver client: {silver_client.get_total_price([10, 15, 20]):.2f}')
    gold_client = Client('Inna', GoldDiscount(today_discount))
    print(f'Gold client: {gold_client.get_total_price([10, 15, 20]):.2f}')

if __name__ == '__main__':
    main()