from project.food.main_dish import MainDish


class Salmon(MainDish):

    def __init__(self, name: str, price: float):
        super().__init__(name, price, 22)
