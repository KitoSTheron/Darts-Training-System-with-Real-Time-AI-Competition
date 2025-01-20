import copy
from ParentGenerator import ParentGenerator

from ParentSelection import get_highest_scoring_object, Creat_child_array
from StochasticGradientDescent import performHeuristic, deep_copy_solution


class AIController:

    def __init__(self, score=None, dartboard=None):
        # super().__init__(master)  # Removed as it is not needed
        self.score = score
        self.dartboard = dartboard

    
    def optimise_throw(self):
        generateParent = ParentGenerator(self.dartboard)
        parents = []

        for i in range(10000):
            parent = generateParent.RandomParentGenerator()
            parents.append(deep_copy_solution(parent))

        for i in range(5):
            for i in range(10000):
                parents[i] = performHeuristic(deep_copy_solution(parents[i]),self.score,self.dartboard)
            parents = Creat_child_array(self.score,deep_copy_solution(parents))

        bestSolution = get_highest_scoring_object(self.score,parents)
        self.dartboard.draw_dart(bestSolution[0][1][0],bestSolution[0][1][1])
        return bestSolution
    
    