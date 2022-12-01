from OOP.classes_and_objects.exercises.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):

        for el in self.tasks:
            if el.name == task_name:
                el.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        cleared = 0
        for tsk in self.tasks:
            if tsk.completed:
                self.tasks.remove(tsk)
                cleared += 1
        return f"Cleared {cleared} tasks."

    def view_section(self):
        result = f'Section {self.name}:\n'
        for t in self.tasks:
            result += f'{t.details()}\n'
        result = result.strip()
        return result

