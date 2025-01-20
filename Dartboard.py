import tkinter as tk
import math

class Dartboard(tk.Canvas):
    WIDTH = 1000
    HEIGHT = 600

    def __init__(self, master=None):
        super().__init__(master, width=Dartboard.WIDTH, height=Dartboard.HEIGHT)
        self.pack(fill=tk.BOTH, expand=True)
        self.scores = [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5]
        self.drawn = False  # Flag to indicate if the dartboard has been drawn
        self.draw_dartboard()
        self.score_list = []
        self.current_dot = None
        self.draw_scoreboard()
    def get_width(self):
        return Dartboard.WIDTH

    def get_height(self):
        return Dartboard.HEIGHT

    def draw_scoreboard(self):
        self.delete("scoreboard")
        x = Dartboard.WIDTH - 150
        y = 100
        self.create_text(x, y, text="Score", font=('Arial', 24, 'bold'), fill='purple', tags="scoreboard")
        bustnum = 0
        for index, score in enumerate(self.score_list):
            if score == -1:
                score_text = "X"
                y_offset = ((index + bustnum) // 3) * 30
                x_offset = ((index + bustnum) % 3) * 50
                self.create_text(x + x_offset, y + y_offset + 30, text=score_text, font=('Arial', 18, 'bold'), fill='purple', tags="scoreboard")
                while (index + bustnum + 1) % 3 != 0:
                    bustnum += 1
                    x_offset = ((index + bustnum) % 3) * 50
                    self.create_text(x + x_offset, y + y_offset + 30, text=score_text, font=('Arial', 18, 'bold'), fill='purple', tags="scoreboard")
            else:
                score_text = str(score)
                y_offset = ((index + bustnum) // 3) * 30
                x_offset = ((index + bustnum) % 3) * 50
                self.create_text(x + x_offset, y + y_offset + 30, text=score_text, font=('Arial', 18, 'bold'), fill='purple', tags="scoreboard")

    def update_scoreboard(self, score, is_bust=False):
        if is_bust:
            self.score_list.append(-1)  # Use -1 to represent a bust
        else:
            self.score_list.append(score)
        self.draw_scoreboard()

    def draw_dartboard(self):
        self.delete("all")
        width = Dartboard.WIDTH
        height = Dartboard.HEIGHT
        center_x = width // 2
        center_y = height // 2
        radius = min(center_x, center_y) - 10

        padding = radius

        self.create_oval(center_x - padding, center_y - padding, center_x + padding, center_y + padding, fill="black")
        padding = radius / 1.15
        self.create_oval(center_x - padding, center_y - padding, center_x + padding, center_y + padding, fill="red")
        padding = radius / 1.25
        self.create_oval(center_x - padding, center_y - padding, center_x + padding, center_y + padding, fill="tan")
        padding = radius / 2
        self.create_oval(center_x - padding, center_y - padding, center_x + padding, center_y + padding, fill="red")
        padding = radius / 2.2
        self.create_oval(center_x - padding, center_y - padding, center_x + padding, center_y + padding, fill="tan")
        padding = radius / 15
        self.create_oval(center_x - padding, center_y - padding, center_x + padding, center_y + padding, fill="green")
        padding = radius / 30
        self.create_oval(center_x - padding, center_y - padding, center_x + padding, center_y + padding, fill="red")

        # Draw the radial lines
        for i in range(20):
            angle = i * (360 / 20)
            angle += 9
            x = center_x + radius * math.cos(math.radians(angle))
            inner_x = center_x + (padding * 2) * math.cos(math.radians(angle))
            y = center_y + radius * math.sin(math.radians(angle))
            inner_y = center_y + (padding * 2) * math.sin(math.radians(angle))
            self.create_line(inner_x, inner_y, x, y, fill='black')

        # Draw the score numbers
        for i, score in enumerate(self.scores):
            angle = i * (360 / 20) - 90
            x = center_x + (radius + 20) * math.cos(math.radians(angle)) * 0.85
            y = center_y + (radius + 20) * math.sin(math.radians(angle)) * 0.85
            self.create_text(x, y, text=str(score), font=('Arial', 12, 'bold'), fill='white')

        self.drawn = True  # Set the flag to True after drawing the dartboard

    def on_click(self, x, y):
        width = Dartboard.WIDTH
        height = Dartboard.HEIGHT
        center_x = width // 2
        center_y = height // 2
        radius = min(center_x, center_y) - 10

        # Define radii for bullseye, bull, double, and triple regions
        bullseye_radius = radius / 30
        bull_radius = radius / 15
        double_ring_outer_radius = radius / 1.15
        double_ring_inner_radius = radius / 1.25
        triple_ring_outer_radius = radius / 2
        triple_ring_inner_radius = radius / 2.2

        # Calculate distance from center
        dx = x - center_x
        dy = y - center_y
        distance = math.sqrt(dx**2 + dy**2)

        # Calculate angle
        angle = (math.degrees(math.atan2(dy, dx)) + 90 + 9) % 360

        # Determine the score based on angle and distance
        if distance <= bullseye_radius:
            return [50, True]
        elif distance <= bull_radius:
            return [25, False]
        elif double_ring_inner_radius <= distance <= double_ring_outer_radius:
            section = int(angle // (360 / 20))
            score = self.scores[section] * 2
            return [score, True]
        elif triple_ring_inner_radius <= distance <= triple_ring_outer_radius:
            section = int(angle // (360 / 20))
            score = self.scores[section] * 3
            return [score, False]
        elif distance <= radius:
            section = int(angle // (360 / 20))
            score = self.scores[section]
            return [score, False]
        else:
            return [0, False]

    def draw_dart(self,x,y):
        # Draw a red dot at the click coordinates
        if self.current_dot:
            self.delete(self.current_dot)
        self.current_dot = self.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")
        
    def on_resize(self, event):
        self.draw_dartboard()
        self.draw_scoreboard()