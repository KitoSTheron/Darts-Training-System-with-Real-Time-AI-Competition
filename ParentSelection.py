from Scorer import score_darts
from StochasticGradientDescent import deep_copy_solution

def get_highest_scoring_object(startingScore,Parents):
    
    
    highest_score = float('-inf')
    highest_scoring_object = None
    
    for Parent in Parents:
        score = score_darts(startingScore,Parent)
        if score > highest_score:
            highest_score = score
            highest_scoring_object = Parent
    
    return highest_scoring_object

def Creat_child_array(startingScore, Parents):
    highest_scores = [float('-inf'), float('-inf')]
    highest_scoring_objects = [None, None]

    for Parent in Parents:
        score = score_darts(startingScore, Parent)
        if score > highest_scores[0]:
            highest_scores[1] = highest_scores[0]
            highest_scoring_objects[1] = highest_scoring_objects[0]
            highest_scores[0] = score
            highest_scoring_objects[0] = Parent
        elif score > highest_scores[1]:
            highest_scores[1] = score
            highest_scoring_objects[1] = Parent
    children = []
    for i in range(4):
        child1 = highest_scoring_objects[0]
        child2 = highest_scoring_objects[1]
        children.append(deep_copy_solution(child1))
        children.append(deep_copy_solution(child2))
    return children
    