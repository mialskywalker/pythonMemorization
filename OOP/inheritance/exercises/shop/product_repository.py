from OOP.inheritance.exercises.shop.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        if self.products:
            for el in self.products:
                if el.name == product_name:
                    return el

    def remove(self, product_name):
        if self.products:
            for el in self.products:
                if el.name == product_name:
                    self.products.remove(el)

    def __repr__(self):
        result = ''
        for el in self.products:
            result += f"{el.name}: {el.quantity}\n"
        result = result.strip()
        return result
