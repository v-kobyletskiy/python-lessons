import product
import cart
import exceptions

if __name__ == '__main__':
    try:
        product_1 = product.Product('Milk', 20)
        product_2 = product.Product('Bread', 10)
        product_3 = product.Product('Meat', 100)

        cart = cart.Cart()
        cart.add_product(product_1, 2)
        cart.add_product(product_2)
        cart.add_product(product_3, 1.5)

        cart.remove_product(product_3, 0.5)
        print(cart)
    except exceptions.InvalidPriceException as err:
        print(err)
