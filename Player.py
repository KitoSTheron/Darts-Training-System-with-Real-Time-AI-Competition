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
    def __init__(self, name, dartboard, playernum):
        super().__init__(name, dartboard)
        self.playernum = playernum
        self.click_occurred = tk.BooleanVar(value=False)
        self.dartboard.master.bind("<Button-1>", self.await_click)

    def throw_dart(self,throwNum,difficulty):
        self.click_occurred.set(False)
        self.dartboard.master.wait_variable(self.click_occurred)
        return self.click_result

    def await_click(self, event):
        x, y = event.x, event.y
        self.click_result = self.dartboard.on_click(x, y)
        self.dartboard.draw_dart(x, y, self.playernum)
        self.click_occurred.set(True)

class AIPlayer(Player):
    def __init__(self, name, dartboard, playernum):
        super().__init__(name, dartboard)
        self.optimisedleg = []
        self.playernum = playernum

    def throw_dart(self,throwNum,difficulty):
        
        if (throwNum == 0):
            controller = AIController(self.score,self.dartboard,difficulty)
            self.optimisedleg = controller.optimise_throw()
        self.dartboard.draw_dart(self.optimisedleg[throwNum][1][0],self.optimisedleg[throwNum][1][1],self.playernum)
        return self.optimisedleg[throwNum][0]