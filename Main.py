import tkinter as tk
from GameLogic import GameLogic
from Dartboard import Dartboard
from Player import HumanPlayer, AIPlayer

class MainMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.start_button = tk.Button(self, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=20)

        self.difficulty_label = tk.Label(self, text="Select Difficulty:")
        self.difficulty_label.pack(pady=10)

        self.difficulty_scale = tk.Scale(self, from_=1, to=167, orient=tk.HORIZONTAL)
        self.difficulty_scale.pack(pady=10)

    def start_game(self):
        difficulty = self.difficulty_scale.get()
        self.pack_forget()  # Hide the main menu
        start_dartboard_game(self.master, difficulty)

def start_dartboard_game(root, difficulty):
    # Create the Dartboard, Players, and GameLogic instances
    dartboard = Dartboard(master=root)
    player1 = HumanPlayer("Player 1", dartboard,0)
    player2 = AIPlayer("Player 2", dartboard,1)
    game_logic = GameLogic(master=root, dartboard=dartboard, player1=player1, player2=player2, difficulty=difficulty)
    
    # Schedule the playGame method to run after the Tkinter event loop starts
    root.after(100, game_logic.playGame)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Dartboard Game")

    # Set the initial dimensions of the window and disable resizing
    initial_width = 1000
    initial_height = 600
    root.geometry(f"{initial_width}x{initial_height}")
    root.resizable(False, False)  # Disable window resizing

    # Create and display the main menu
    main_menu = MainMenu(master=root)
    main_menu.pack()

    root.mainloop()