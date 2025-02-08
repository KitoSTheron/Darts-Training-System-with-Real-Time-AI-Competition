import random
import numpy as np
from Scorer import score_darts

def optimise_throw(dartboard, start_score,difficulty):
    num_ants = int(difficulty/ 8)
    num_iterations = int(difficulty/ 6)
    evaporation_rate = 0.1
    pheromone_deposit_factor = 100
    radius = 290
    grid_size = 600
    epsilon = 1e-6  # Small bias to avoid division by zero

    # Initialize the pheromones grid
    pheromones = np.full((grid_size, grid_size), epsilon)

    for iteration in range(num_iterations):
        solutions = []
        scores = []
        for ant in range(num_ants):
            # Generate coordinates for 3 darts influenced by pheromones
            coordinates = []
            for _ in range(3):
                x = 500 + random.uniform(-290,+290)
                y = 300 + random.uniform(-290,+290)
                #x, y = select_coordinate_with_pheromones(pheromones, radius, grid_size)

                coordinates.append((x, y))

            # Process coordinates separately in the on_click function
            on_click_results = [dartboard.on_click(x, y) for x, y in coordinates]

            # Concatenate the outputs and input into the score_darts function
            score = score_darts(start_score, [[on_click_results[0], coordinates[0]], [on_click_results[1], coordinates[1]], [on_click_results[2], coordinates[2]]])

            if score == -1:
                continue
            solutions.append([[on_click_results[i], coordinates[i]] for i in range(3)])
            scores.append(score)

        # Evaporate pheromones
        pheromones *= (1 - evaporation_rate)

        # Update pheromones based on solutions and scores
        for solution, score in zip(solutions, scores):
            for (on_click_result, (x, y)) in solution:
                i = min(max(int((x / 1000) * (grid_size - 1)), 0), grid_size - 1)
                j = min(max(int((y / 600) * (grid_size - 1)), 0), grid_size - 1)
                pheromones[i, j] += pheromone_deposit_factor * score

    if scores:
        max_score = max(scores)
        best_index = scores.index(max_score)
        best_solution = solutions[best_index]
        print(f"Best score: {max_score}, Best solution: {best_solution}")
        return best_solution

def select_coordinate_with_pheromones(pheromones, radius, grid_size):
    # Flatten the pheromones grid and normalize to create a probability distribution
    flat_pheromones = pheromones.flatten()
    total_pheromones = np.sum(flat_pheromones)
    probabilities = flat_pheromones / total_pheromones

    # Select a grid cell based on the pheromone probability distribution
    selected_index = np.random.choice(len(flat_pheromones), p=probabilities)
    i = selected_index // grid_size
    j = selected_index % grid_size

    # Convert grid cell to coordinates within the radius
    x = (i / (grid_size - 1)) * 1000
    y = (j / (grid_size - 1)) * 600
    x += random.uniform(-radius, radius)
    y += random.uniform(-radius, radius)
    return x, y

# Example usage
if __name__ == "__main__":
    import tkinter as tk
    from Dartboard import Dartboard

    root = tk.Tk()
    dartboard = Dartboard(master=root)
    best_solution = optimise_throw(dartboard, 501)
    print(f"Returned best solution: {best_solution}")