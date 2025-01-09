import tkinter as tk

class Player:
    def __init__(self, name, dartboard):
        self.name = name
        self.score = 501
        self.dartboard = dartboard

    def throw_dart(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class HumanPlayer(Player):
    def __init__(self, name, dartboard):
        super().__init__(name, dartboard)
        self.click_occurred = tk.BooleanVar(value=False)
        self.dartboard.master.bind("<Button-1>", self.await_click)

    def throw_dart(self):
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

    def throw_dart(self):
        # Implement logic for AI player throwing a dart
        print(f"{self.name} (AI) throws a dart!")