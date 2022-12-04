from OOP.class_and_static_methods.exercises.project.customer import Customer
from OOP.class_and_static_methods.exercises.project.equipment import Equipment
from OOP.class_and_static_methods.exercises.project.exercise_plan import ExercisePlan
from OOP.class_and_static_methods.exercises.project.subscription import Subscription
from OOP.class_and_static_methods.exercises.project.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return
        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan in self.plans:
            return
        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = [el for el in self.subscriptions if el.id == subscription_id][0]
        customer = [el for el in self.customers if el.id == subscription.customer_id][0]
        trainer = [el for el in self.trainers if el.id == subscription.trainer_id][0]
        plan = [el for el in self.plans if el.id == trainer.id][0]
        equipment = [el for el in self.equipment if el.id == plan.id][0]
        result = f"{subscription.__repr__()}\n" \
                 f"{customer.__repr__()}\n" \
                 f"{trainer.__repr__()}\n" \
                 f"{equipment.__repr__()}\n" \
                 f"{plan.__repr__()}"
        return result
