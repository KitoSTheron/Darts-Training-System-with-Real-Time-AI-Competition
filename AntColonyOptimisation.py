import random
import numpy as np
from Scorer import score_darts

def optimise_throw(dartboard, start_score,difficulty):
    num_ants = int(difficulty/ 4)
    num_iterations = int(difficulty/ 3)
    evaporation_rate = 0.1
    pheromone_deposit_factor = 100
    radius = 290
    grid_size = 60
    epsilon = np.finfo(float).eps

    # Initialize the pheromones grid
    pheromones = np.full((grid_size, grid_size), epsilon)

    for iteration in range(num_iterations):
        solutions = []
        scores = []
        for ant in range(num_ants):
            # Generate coordinates for 3 darts influenced by pheromones
            coordinates = []
            on_click_results = []
            for _ in range(3):
                #x = 500 + random.uniform(-290,+290)
                #y = 300 + random.uniform(-290,+290)
                x, y = select_coordinate_with_pheromones(pheromones, grid_size)

                coordinates.append((x, y))
                on_click_results.append(dartboard.on_click(x, y))



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

def select_coordinate_with_pheromones(pheromones, grid_size):
    # Flatten the pheromones grid and normalize to create a probability distribution
    flat_pheromones = pheromones.flatten()
    total_pheromones = np.sum(flat_pheromones)
    probabilities = flat_pheromones / total_pheromones

    # Select an index based on the probability distribution
    selected_index = np.random.choice(len(flat_pheromones), p=probabilities)

    # Convert the flat index back to 2D grid coordinates
    i = selected_index // grid_size
    j = selected_index % grid_size

    # Scale the coordinates to the dartboard size
    x = i*10 + 200
    y = j*10

    return x, y

# Example usage

#if __name__ == "__main__":
#    import tkinter as tk
#    from Dartboard import Dartboard

#    root = tk.Tk()
#    dartboard = Dartboard(master=root)
#    best_solution = optimise_throw(dartboard, 501, 167)
#    print(f"Returned best solution: {best_solution}")