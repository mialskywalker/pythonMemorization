from collections import defaultdict

from OOP.encapsulation.exercises.pizza_maker.dough import Dough
from OOP.encapsulation.exercises.pizza_maker.topping import Topping


class Pizza:

    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = defaultdict(lambda: 0)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("The name cannot be an empty string")
        self._name = value

    @property
    def dough(self):
        return self._dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self._dough = value

    @property
    def toppings_capacity(self):
        return self._toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self._toppings_capacity = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) >= self.toppings_capacity:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings.keys():
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        if self.toppings:
            toppings_weight = sum([el for el in self.toppings.values()])
            dough_weight = self.dough.weight
            total_weight = toppings_weight + dough_weight
            return total_weight
