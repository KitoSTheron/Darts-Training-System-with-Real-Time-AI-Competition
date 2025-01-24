import random
from Scorer import score_darts

def optimise_throw(dartboard,start_score):
    num_ants = 20
    num_iterations = 50
    pheromone_influence = 1
    heuristic_influence = 2
    evaporation_rate = 0.1
    pheromone_deposit_factor = 100
    radius = 290
    grid_size = 600

    # Pheromones grid
    pheromones = [[0.1 for _ in range(grid_size)] for _ in range(grid_size)]  # Small initial pheromone values

    for iteration in range(num_iterations):
        solutions = []
        scores = []

        for ant in range(num_ants):
            # Darts chosen for each ant
            candidates = []
            # Odds of an ant moving to that part of the board
            probabilities = []

            for _ in range(20):  # Ant generates 20 candidate throws to choose from
                x = 500 + random.uniform(-radius, +radius)
                y = 300 + random.uniform(-radius, +radius)

                score = score_darts(start_score,[[dartboard.on_click(x, y),[x,y]],[[0,False],[0,0]],[[0,False],[0,0]]])

                # Calculate pheromone and heuristic values
                i = int((x / 1000) * (grid_size - 1))
                j = int((y / 600) * (grid_size - 1))
                pheromone = pheromones[i][j]
                heuristic = score
                # Calculate where the ant should go based on pheromone + score
                combined_value = (pheromone ** pheromone_influence) * (heuristic ** heuristic_influence)
                candidates.append((x, y, score, combined_value))
                probabilities.append(combined_value)

            # Normalize probabilities to make them a valid probability distribution
            total_prob = sum(probabilities)
            if total_prob == 0:
                continue  # No valid throws this iteration
            probabilities = [p / total_prob for p in probabilities]

            # Use roulette wheel selection to pick a throw based on probabilities
            cumulative_prob = 0
            rand_val = random.uniform(0, 1)
            chosen_index = -1
            for index, prob in enumerate(probabilities):
                cumulative_prob += prob
                if rand_val <= cumulative_prob:
                    chosen_index = index
                    break

            if chosen_index == -1:
                continue  # No valid throw selected

            # Add the chosen throw to the solutions
            x, y, score, _ = candidates[chosen_index]
            solutions.append([x, y])
            scores.append(score)

        # Evaporate pheromones
        pheromones = [[pheromone * (1 - evaporation_rate) for pheromone in row] for row in pheromones]

        # Update pheromones based on solutions and scores
        for [x, y], score in zip(solutions, scores):
            i = int((x / 1000) * (grid_size - 1))
            j = int((y / 600) * (grid_size - 1))
            pheromones[i][j] += pheromone_deposit_factor * score

    # Find the best solution
    if scores:
        max_score = max(scores)
        best_index = scores.index(max_score)
        best_solution = solutions[best_index]
    return best_solution

# Example usage
if __name__ == "__main__":
    import tkinter as tk
    from Dartboard import Dartboard

    root = tk.Tk()
    dartboard = Dartboard(master=root)
    print(optimise_throw(dartboard,501))