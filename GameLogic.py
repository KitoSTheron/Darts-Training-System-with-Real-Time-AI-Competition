import tkinter as tk
from AIFeatures.ParentGenerator import ParentGenerator

gameOver = 0
bust = 1
nextThrow = 2

class GameLogic(tk.Frame):
    def __init__(self, master=None, dartboard=None, player=None):
        super().__init__(master)
        self.dartboard = dartboard
        self.player = player

    def playGame(self):
        status = -1
        while(status != 0):
            originalScore = self.player.score
            for i in range(3):
                if i == 0 and self.dartboard.current_dot:
                    self.dartboard.delete(self.dartboard.current_dot)
                    self.dartboard.current_dot = None
                hitStats = self.player.throw_dart()
                status = self.HandleThrow(hitStats[0], hitStats[1])
                if (status == gameOver):
                    self.dartboard.update_scoreboard(hitStats[0])
                    status = 0  # Exit the while loop
                    break
                elif (status == bust):
                    self.player.score = originalScore
                    self.dartboard.update_scoreboard(-1)
                    break
                elif (status == nextThrow):
                    self.player.score -= hitStats[0]
                    self.dartboard.update_scoreboard(hitStats[0])
                print(self.player.score)
        print("Game Over")

    def HandleThrow(self, hitValue, isDouble):
        if ((self.player.score - hitValue == 0) and isDouble):
            return gameOver
        elif (self.player.score - hitValue <= 1):
            return bust
        else:
            return nextThrow