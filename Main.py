import tkinter as tk
from GameLogic import GameLogic
from Dartboard import Dartboard
from Player import HumanPlayer, AIPlayer


if __name__ == "__main__":

    root = tk.Tk()
    dartboard = Dartboard(master=root)
    player = HumanPlayer("player1", dartboard)
    game_logic = GameLogic(master=root, dartboard=dartboard, player=player)
    game_logic.playGame()
    root.mainloop()