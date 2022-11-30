class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        if self.get_empty_space() < ml:
            return f"Cannot add {ml} ml"

        self.content += ml
        return f"Glass filled with {ml} ml"

    def get_empty_space(self):
        return Glass.capacity - self.content

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{self.get_empty_space()} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
