from ParentGenerator import ParentGenerator

from StochasticGradientDescent import performHeuristic


class AIController:

    def __init__(self, score=None, dartboard=None):
        # super().__init__(master)  # Removed as it is not needed
        self.score = score
        self.dartboard = dartboard


    def optimise_throw(self):
        generateParent = ParentGenerator(self.dartboard)
        solution = generateParent.RandomParentGenerator()
        improved = False
        newsolution = solution
        while improved == False:
            newsolution = performHeuristic(solution,self.score,self.dartboard)
            if (newsolution != solution):
                improved = True
        self.dartboard.draw_dart(newsolution[0][1][0],newsolution[0][1][1])
        print(newsolution)
        return newsolution
    
    