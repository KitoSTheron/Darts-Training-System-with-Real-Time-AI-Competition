import tkinter as tk
import math

class Dartboard(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master, width=600, height=600)
        self.pack(fill=tk.BOTH, expand=True)
        self.bind("<Configure>", self.on_resize)
        self.scores = [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5]
        self.draw_dartboard()

    def draw_dartboard(self):
        self.delete("all")
        width = self.winfo_width()
        height = self.winfo_height()
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

    def on_click(self, x, y):
        width = self.winfo_width()
        height = self.winfo_height()
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
            return [50,True]
        elif distance <= bull_radius:
            return [25,False]
        elif double_ring_inner_radius <= distance <= double_ring_outer_radius:
            section = int(angle // (360 / 20))
            score = self.scores[section] * 2
            return [score,True]
        elif triple_ring_inner_radius <= distance <= triple_ring_outer_radius:
            section = int(angle // (360 / 20))
            score = self.scores[section] * 3
            return [score,False]
        elif distance <= radius:
            section = int(angle // (360 / 20))
            score = self.scores[section]
            return [score,False]
        else:
            return [0,False]

    def on_resize(self, event):
        self.draw_dartboard()