import random
import copy
from Scorer import score_darts
from Dartboard import Dartboard

def performHeuristic(solution, startingScore, dartboard):

    newSolution = deep_copy_solution(solution)  # Deep copy for newSolution
    candidateSolution = deep_copy_solution(solution)  # Deep copy for candidateSolution
    myDartboard = dartboard
    cumulativescore = 0
    for i in range(3):
        if random.random() < 0.8:
            candidateSolution[i][1] = best_improvement(candidateSolution[i][1][0], candidateSolution[i][1][1], startingScore - cumulativescore, dartboard)
        else:
            candidateSolution[i][1] = random_neighbour(candidateSolution[i][1][0], candidateSolution[i][1][1])
        candidateSolution[i][0] = dartboard.on_click(candidateSolution[i][1][0], candidateSolution[i][1][1])
        cumulativescore += solution[i][0][0]
        if score_darts(startingScore, candidateSolution) > score_darts(startingScore, newSolution):
            newSolution = deep_copy_solution(candidateSolution)  # Deep copy to ensure isolation
            candidateSolution = deep_copy_solution(solution)  # Reset candidateSolution to the initial state
    return newSolution

def deep_copy_solution(solution):
    if solution is None:
        return None
    return [[item.copy() if isinstance(item, list) else item for item in sublist] for sublist in solution]

def best_improvement(x,y,score,dartboard):
    bestscore = 0
    bestsolution = [0,0]
    for i in range(500 - 290, 500 + 290, random.randint(1,50)):
        for j in range(300 - 290, 300 + 290, random.randint(1,50)):
            dartscore = dartboard.on_click(i,j)
            candidate = score_darts(score , [[[dartscore[0],dartscore[1]],[i,j]]])
            if candidate > bestscore:
                bestsolution = [i,j]
                bestscore = candidate
    return bestsolution


def random_neighbour(x, y):
    x = x + random.randint(-300, 300)
    y = y + random.randint(-300, 300)
    return [x, y]