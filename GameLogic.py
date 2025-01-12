import math
import tkinter as tk

from traitlets import This

from Dartboard import Dartboard
from Player import Player

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
            hitStats = self.player.throw_dart()
            status = self.HandleThrow(hitStats[0], hitStats[1])
            if (status == 2):
                self.player.score -= hitStats[0]
            print(self.player.score)
        print("Game Over")
        
        
    def HandleThrow(self, hitValue, isDouble):
        if ((self.player.score - hitValue == 0) and isDouble):
            return gameOver
        elif (self.player.score - hitValue <= 1):
            return bust
        else:
            return nextThrow

    