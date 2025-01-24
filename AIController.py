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
        generateParent = ParentGenerator(self.dartboard,self)
        parents = []

        for i in range(4):
            parent = generateParent.AntParentGenerator()
            parents.append(deep_copy_solution(parent))

        for i in range(5):
            for i in range(4):
                parents[i] = performHeuristic(deep_copy_solution(parents[i]),self.score,self.dartboard)
            parents = Creat_child_array(self.score,deep_copy_solution(parents))

        bestSolution = get_highest_scoring_object(self.score,parents)
        return bestSolution
    
    