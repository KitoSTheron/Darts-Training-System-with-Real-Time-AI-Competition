import tkinter as tk
import math
from Dartboard import Dartboard
from GameLogic import GameLogic
from Player import Player
from Player import HumanPlayer

if __name__ == "__main__":

    root = tk.Tk()
    root.title("Dartboard")
    dartboard = Dartboard(master=root)
    player = HumanPlayer(name="Player 1", dartboard=dartboard)
    rules = GameLogic(master=root, dartboard=dartboard, player = player)
    rules.playGame()
    
    root.mainloop()