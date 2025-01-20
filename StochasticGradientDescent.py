import random
import copy
from Scorer import score_darts
from Dartboard import Dartboard

def performHeuristic(solution, startingScore, dartboard):

    newSolution = deep_copy_solution(solution)  # Deep copy for newSolution
    candidateSolution = deep_copy_solution(solution)  # Deep copy for candidateSolution
    myDartboard = dartboard

    for i in range(3):
        candidateSolution[i][1] = random_neighbour(solution[i][1][0], solution[i][1][1])
        candidateSolution[i][0] = Dartboard.on_click(myDartboard, candidateSolution[i][1][0], candidateSolution[i][1][1])
        
        if score_darts(startingScore, candidateSolution) > score_darts(startingScore, newSolution):
            newSolution = deep_copy_solution(candidateSolution)  # Deep copy to ensure isolation
            candidateSolution = deep_copy_solution(solution)  # Reset candidateSolution to the initial state
    return newSolution

def deep_copy_solution(solution):
    return [[item.copy() if isinstance(item, list) else item for item in sublist] for sublist in solution]

def random_neighbour(x, y):
    x = x + random.randint(-300, 300)
    y = y + random.randint(-300, 300)
    return [x, y]