class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product_name):
        Catalogue.products.append(product_name)

    def get_by_letter(self, first_letter):
        return list(filter(lambda el: el[0] == first_letter, Catalogue.products))

    def __repr__(self):
        return f"Items in the {self.name} catalogue:\n" + '\n'.join(sorted(Catalogue.products))


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)