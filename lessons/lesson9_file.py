from typing import List


def read_purchases(path: str) -> List[str]:
    """

    :param path: file path
    :return: list of purchase strings
    """
    purchases = []
    with open(path, 'rt', encoding='utf-8') as file:
        for line in file:
            purchases.append(line.strip())
    return purchases


def collect_categories(purchases: List[str]):
    """

    :param purchases: list of purchases
    :return: dictionary with category as key and money spent as value
    """
    category_storage = {}
    for purchase in purchases:
        purchase_item = get_purchase_item(purchase)
        category, money = purchase_item['category'], purchase_item['money']
        category_storage[category] = category_storage.get(category, 0) + money
    return category_storage


def collect_people(purchases: List[str]):
    """

    :param purchases: list of purchase strings
    :return: dictionary with name as key and money spent as value
    """
    people_storage = {}
    for purchase in purchases:
        purchase_item = get_purchase_item(purchase)
        name, money = purchase_item['name'], purchase_item['money']
        people_storage[name] = people_storage.get(name, 0) + money
    return people_storage


def collect_people_purchases(purchases: List[str]):
    """

    :param purchases: list of purchase strings
    :return: dictionary with name as key and dictionary category:spent money as value
    """
    people_purchases = {}
    for purchase in purchases:
        name, category, money = get_purchase_item(purchase).values()
        if not people_purchases.get(name):
            people_purchases[name] = {}
        human_purchases = people_purchases.get(name)
        category_purchases = human_purchases.get(category, 0)
        people_purchases[name][category] = category_purchases + money
    return people_purchases


def get_purchase_item(purchase: List[str]):
    """

    :param purchase: list of purchase strings
    :return: dictionary with 'name', 'category', 'money' of purchase
    """
    return {
        'name': get_name(purchase),
        'category': get_category(purchase),
        'money': get_money(purchase)
    }


def get_purchase_data(purchase: str):
    """

    :param purchase: string from purchase file
    :return: purchase string split by spaces
    """
    return purchase.split()


def get_money(purchase: str):
    """

    :param purchase: string from purchase file
    :return: money spent by purchase
    """
    purchase_data = get_purchase_data(purchase)
    return float(purchase_data[-2].replace('$', ''))


def get_category(purchase: str):
    """

    :param purchase: string from purchase file
    :return: category of purchase
    """
    return get_purchase_data(purchase)[-1]


def get_name(purchase: str):
    """

    :param purchase: string from purchase file
    :return: name of family member
    """
    purchase_data = get_purchase_data(purchase)
    surname_present = not purchase_data[-4].isdigit()
    name_data = purchase_data[-3:-5 if surname_present else -4:-1]
    return ' '.join(name_data[::-1])


def print_storage(storage: dict, header: str):
    """

    :param storage: dictionary with data
    :param header: caption before data output
    :return: None
    """
    print(f'\n{header}')
    for item in storage:
        print(f'{item}: {storage[item]:.2f}$')


def print_family_member_purchases(member_name: str, purchases: List[str]):
    """
    Function prints purchases of family member grouped by category and total
    :param member_name: name of family member
    :param purchases: list of purchase strings
    :return: None
    """
    people_purchases = collect_people_purchases(purchases)
    family_member_purchases = people_purchases.get(member_name)
    if family_member_purchases:
        print(f'Name: {member_name} purchases: {family_member_purchases}'
              f' total amount: {sum([family_member_purchases[category] for category in family_member_purchases])}')
    else:
        print('No family member found')


def main():
    purchases = read_purchases('hw_10_test.txt')
    people_storage = collect_people(purchases)
    print_storage(collect_categories(purchases), '***Categories***')
    print_storage(people_storage, '***People purchases***')
    member_name = input('Please enter name>>>')
    print_family_member_purchases(member_name, purchases)


if __name__ == '__main__':
    main()

# def func_pow(digit, degree):
#     if degree == 1:
#         return digit
#     return digit * func_pow(digit, degree - 1)
#
# print(func_pow(2, 4))
