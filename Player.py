import tkinter as tk
from AIController import AIController
from ParentGenerator import ParentGenerator
from StochasticGradientDescent import performHeuristic


class Player:
    def __init__(self, name, dartboard):
        self.name = name
        self.score = 501
        self.dartboard = dartboard

    def throw_dart(self,throwNum):
        raise NotImplementedError("This method should be overridden by subclasses")

class HumanPlayer(Player):
    def __init__(self, name, dartboard):
        super().__init__(name, dartboard)
        self.click_occurred = tk.BooleanVar(value=False)
        self.dartboard.master.bind("<Button-1>", self.await_click)

    def throw_dart(self,throwNum):
        self.click_occurred.set(False)
        self.dartboard.master.wait_variable(self.click_occurred)
        return self.click_result

    def await_click(self, event):
        x, y = event.x, event.y
        self.click_result = self.dartboard.on_click(x, y)
        self.click_occurred.set(True)

class AIPlayer(Player):
    def __init__(self, name, dartboard):
        super().__init__(name, dartboard)
        self.optimisedleg = []
    def throw_dart(self,throwNum):
        
        print(f"{self.name} (AI) throws a dart!")
        if (throwNum == 0):
            controller = AIController(self.score,self.dartboard)
            self.optimisedleg = controller.optimise_throw()
        return self.optimisedleg[throwNum][0]