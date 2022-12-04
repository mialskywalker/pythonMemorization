class ExercisePlan:

    ID = 0

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        ExercisePlan.ID += 1
        self.id = ExercisePlan.ID

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        hours_to_mins = hours * 60
        return cls(trainer_id, equipment_id, hours_to_mins)

    @staticmethod
    def get_next_id():
        return ExercisePlan.ID + 1
