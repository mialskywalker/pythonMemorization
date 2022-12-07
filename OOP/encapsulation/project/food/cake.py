from project.food.dessert import Dessert


class Cake(Dessert):

    def __init__(self, name: str):
        super().__init__(name, 5, 250, 1000)
