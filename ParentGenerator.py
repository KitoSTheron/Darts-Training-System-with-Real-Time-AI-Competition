import random

class ParentGenerator:
    def __init__(self, dartboard):
        self.dartboard = dartboard


    def RandomParentGenerator(self):
        coordinates = []
        for _ in range(3):
            x = 500 + random.uniform(-290,+290)
            y = 300 + random.uniform(-290,+290)
            on_click_result = self.dartboard.on_click(x, y)
            coordinates.append([on_click_result, [x, y]])
        return coordinates


