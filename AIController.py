import copy
from ParentGenerator import ParentGenerator

from ParentSelection import get_highest_scoring_object, Creat_child_array
from StochasticGradientDescent import performHeuristic, deep_copy_solution


class AIController:

    def __init__(self, score=None, dartboard=None, difficulty=None):
        # super().__init__(master)  # Removed as it is not needed
        self.score = score
        self.dartboard = dartboard
        self.difficulty = difficulty

    def highest_even_number(self, n):
        if n % 2 == 0:
            return max(n, 2)
        else:
            return max(n - 1, 2)
        
    def optimise_throw(self):
        generateParent = ParentGenerator(self.dartboard,self,self.difficulty)
        parents = []
        if (self.difficulty < 50):
            parent = generateParent.RandomParentGenerator()
        else:
            parent = generateParent.AntParentGenerator()
        for _ in range(self.highest_even_number((int(self.difficulty/20)))):
            parents.append(deep_copy_solution(parent))


        for _ in range(max(int(self.difficulty/40),1)):
            for j in range(len(parents)):
                parents[j] = performHeuristic(deep_copy_solution(parents[j]),self.score,self.dartboard,self.difficulty)
            parents = Creat_child_array(self.score,deep_copy_solution(parents),len(parents))

        bestSolution = get_highest_scoring_object(self.score,parents)
        return bestSolution
    
    