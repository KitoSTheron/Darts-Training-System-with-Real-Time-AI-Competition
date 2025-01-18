
import random


class ParentGenerator:
    def __init__(self,dartboard):
        self.dartboard = dartboard

    def RandomParentGenerator(self):
        coordinates = []
        for _ in range(3):
            x = random.uniform(0, self.dartboard.get_width())
            y = random.uniform(0, self.dartboard.get_width())
            coordinates.append(self.dartboard.on_click(x, y))

        return coordinates


