import random
from AntColonyOptimisation import optimise_throw

class ParentGenerator:
    def __init__(self, dartboard, player, difficulty):
        self.dartboard = dartboard
        self.player = player
        self.difficulty = difficulty

    def AntParentGenerator(self):
        return optimise_throw(self.dartboard,self.player.score,self.difficulty)
    
    def RandomParentGenerator(self):
        coordinates = []
        for _ in range(3):
            x = 500 + random.uniform(-290,+290)
            y = 300 + random.uniform(-290,+290)
            on_click_result = self.dartboard.on_click(x, y)
            coordinates.append([on_click_result, [x, y]])
        return coordinates


