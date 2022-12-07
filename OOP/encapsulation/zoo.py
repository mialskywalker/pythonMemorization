class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity <= len(self.animals):
            return f"Not enough space for animal"
        if self.__budget < price:
            return f"Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return f"Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker = [el for el in self.workers if el.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        if self.workers:
            total_salary = sum([el.salary for el in self.workers])
            if self.__budget < total_salary:
                return "You have no budget to pay your workers. They are unhappy"
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        if self.animals:
            animals_tending = sum([el.money_for_care for el in self.animals])
            if self.__budget < animals_tending:
                return "You have no budget to tend the animals. They are unhappy."
            self.__budget -= animals_tending
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [el for el in self.animals if el.__class__.__name__ == 'Lion']
        cheetahs = [el for el in self.animals if el.__class__.__name__ == 'Cheetah']
        tigers = [el for el in self.animals if el.__class__.__name__ == 'Tiger']

        result = f"You have {len(self.animals)} animals\n"
        result += f"----- {len(lions)} Lions:\n"
        if lions:
            for el in lions:
                result += f"{type(el).__repr__(el)}\n"
        result += f"----- {len(tigers)} Tigers:\n"
        if tigers:
            for el in tigers:
                result += f"{type(el).__repr__(el)}\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        if cheetahs:
            for el in cheetahs:
                if el == cheetahs[-1]:
                    result += f"{type(el).__repr__(el)}"
                else:
                    result += f"{type(el).__repr__(el)}\n"

        return result

    def workers_status(self):
        if self.workers:
            result = ""
            result += f"You have {len(self.workers)} workers\n"
            keepers = [k for k in self.workers if type(k).__name__ == "Keeper"]
            caretakers = [c for c in self.workers if type(c).__name__ == "Caretaker"]
            vets = [v for v in self.workers if type(v).__name__ == "Vet"]
            result += f"----- {len(keepers)} Keepers:\n"
            if keepers:
                for el in keepers:
                    result += f"{type(el).__repr__(el)}\n"
            result += f"----- {len(caretakers)} Caretakers:\n"
            if caretakers:
                for el in caretakers:
                    result += f"{type(el).__repr__(el)}\n"
            result += f"----- {len(vets)} Vets:\n"
            if vets:
                for el in vets:
                    if el == vets[-1]:
                        result += f"{type(el).__repr__(el)}"
                    else:
                        result += f"{type(el).__repr__(el)}\n"
            return result
