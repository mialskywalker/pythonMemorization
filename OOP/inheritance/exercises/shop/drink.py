from OOP.inheritance.exercises.shop.product import Product


class Drink(Product):

    def __init__(self, name):
        super().__init__(name, quantity=10)
