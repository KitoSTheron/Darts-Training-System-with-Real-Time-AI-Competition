import tkinter as tk
from ParentGenerator import ParentGenerator

gameOver = 0
bust = 1
nextThrow = 2

class GameLogic(tk.Frame):
    def __init__(self, master=None, dartboard=None, player1=None, player2=None, difficulty = None):
        super().__init__(master)
        self.dartboard = dartboard
        self.players = [player1, player2]
        self.current_player_index = 0
        self.difficulty = difficulty

    def playGame(self):
        status = -1
        while(status != 0):
            current_player = self.players[self.current_player_index]
            originalScore = current_player.score
            for i in range(3):
                hitStats = current_player.throw_dart(i,self.difficulty)
                status = self.HandleThrow(hitStats[0], hitStats[1],self.current_player_index)
                if (status == gameOver):
                    current_player.score = 0
                    if (self.current_player_index == 0):
                        self.dartboard.player1_score = current_player.score
                    else:
                        self.dartboard.player2_score = current_player.score
                    self.dartboard.update_scoreboard(hitStats[0],self.current_player_index,status == bust)
                    status = 0  # Exit the while loop
                    break
                elif (status == bust):
                    current_player.score = originalScore
                    if (self.current_player_index == 0):
                        self.dartboard.player1_score = current_player.score
                    else:
                        self.dartboard.player2_score = current_player.score
                    self.dartboard.update_scoreboard(-1,self.current_player_index,status == bust)
                    break
                elif (status == nextThrow):
                    current_player.score -= hitStats[0]
                    if (self.current_player_index == 0):
                        self.dartboard.player1_score = current_player.score
                    else:
                        self.dartboard.player2_score = current_player.score
                    self.dartboard.update_scoreboard(hitStats[0],self.current_player_index,status == bust)
            # Switch to the next player
            self.current_player_index = (self.current_player_index + 1) % 2
            # Give half a second for the GUI to update
            self.update_idletasks()
            self.after(500)
        print("Game Over")

    def HandleThrow(self, hitValue, isDouble,playerIndex):
        if ((self.players[playerIndex].score - hitValue == 0) and isDouble):
            return gameOver
        elif (self.players[playerIndex].score - hitValue <= 1):
            return bust
        else:
            return nextThrow