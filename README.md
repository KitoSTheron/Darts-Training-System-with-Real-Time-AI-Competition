# Darts Training System with Real Time AI Comptetition

## Description

This project allows players to play a game of 501 in darts against an AI Darts player with customisable difficulty and then play a game of darts against that player in real time. The real life player would be playing on a real life dart board and click on the virtual board where they hit in real life and the AI player would take their turn after each leg. The program allows player to keep track of their score also and the game ends when a player wins.

## How to run

The program is run from the Main.py file, from there a menu will be loaded where you can select the difficulty of the AI (1 being easiest and 167 being hardest) the hardness score is meant to represent the average score of the AI each leg however it isn't completely accurate.
If you want to customise which player is AI and which player is human you can adjust the player1 and player2 variables in the Main.py file to AIPlayer or HumanPlayer, this mean you could easily change my game to be a 1vs1 with humans or even two AI players playing against eachother.

## How the program works

When the start button is pressed the screen transitions to the dartboard screen which is initilised in the Dartboard.py file, this file handles drawing the dartboard, drawing the scores by the dartboard and understanding where on the dartboard has been hit after a player takes a turn. The dartboard is drawn by creating a number of ovals inside of eachother with black lines seperating differnt sections such that it looks like a dartboard. To draw the scores around the dartboard I created this array with all of the possible socres you can get on a dartboard in the order that they appear  (from 0 degrees to 360) [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5] and then calculated the angle they should be drawn at which was 360/len(numbers) and that was drawn a little more than the radius away from the center of the dartboard.

The GameLogic.py is the controller which handles the game logic, this file keeps track of which players turn it is and then executes their turn and passes required information between the dartboard and players which is necessary. This file is responsible for knowing if a throw is a bust a win or a regular shot and appropriately responding to that information.

The Player class has two subclasses, AIPlayer and HumanPlayer. They both use the throw_dart method which is called in GameLogic.py.
- The throw_dart method in the HumanPlayer awaits the user to click on the screen and when they have clicked it runs the on_click(x,y) function in the dartboard which returns the score of the click and if it was a double or not.

- The throw_dart method for the AIPlayer will call the AIController on the first turn (which will return all 3 of the next shots) and the function will return the first index and then the next two times it is called the next two indexs will be returned without the need to call the AIController again until the next leg.

## How the AI Works

The AI is handled in the AIController which
1. Initialises parents

   - If the difficulty of the AI is set to less than 50, parent solutions are created by a random generator which throws 3 random darts at the board (using the RandomParentGenerator in the ParentGenerator.py file). This parent is cloned (diffuclty/20) times to create the initial parent array.

   - If the difficulty is greater or equal to 50 them the parents are created using AntColonyOptimisation. The logic for the AntColonyOptimisaiton is in the AntColonyOptimisation.py file, the algorithm is run by the optimise throw function which is called in AntParentGenerator in the ParentGenerator.py file. This parent is cloned (diffuclty/20) times to create the initial parent array

     - This is how Ant Colony Optimisation works in my program: A number of 'ants' explore the serach space (the dartboard) and return a score for the area of the board which they explore, in my case these ants explore in sets of 3 because I need to calculate the score for 3 turns. When ants explore an area of the dartboard they leave a pheromone which is stronger based on how high the score was in that area, future ants are more likely to explore areas of the search space which have higher pheromone values which means the ants tend to get higher scores. In order to ensure ants explore a variety of areas on the board the phoeromones evaporate by 10% after each generation of ants. This algorithm is based on how real ants use pheromones to find the shortest path between their colonies and food spots but I thought it would be interesting to apply it to this project to find hotspots for high scores on the dartboard. The scoring function is found in my Scorer.py file. This algorithm originally proved to be very computationally expensive so was slowing down my program but I later made adjustments to limit this. These adjustments included using the numpy library for faster array handling and reucing the size of the ant grid where every pixel represented 10*10 pixels. The best solution found is finally returned as the parent solution, the parameters used in this algorithm vary based on the AI difficulty. The number of ants is difficulty/4 and the number of iterations is difficulty/3.

3. Runs genetic algorithm (with heuristic)

   - This iterates difficulty/40 times, all parent solutions run a Stochastic Gradient Descent algorithm to improve their solution, the best two parents from the array are chosen to be cloned as children to be the parents for the following generation (this is done in the Create_child_array function written in ParentSelection.py) I chose the best two parents to populat the next generation to add some variation to the solutions.
     - My Stochastic gradient descent algorithm works in the following way: Handled in the StochasticGradientDescent.py file each of the 3 throws of the leg have the best_improvement function applied to them and the one which improves the overal score the most is the change which is kept (20% of the time I run a random neighbor function which selects a nearby area on the dartboard as the improvement, I did this to implement some form of mutations).
       - The best_improvement algorithm doesn't actually always find the absolute best improvement. It scans the dartboard at random intervals (the potential interval size is set by the users difficulty) and finds the best score at every point on the board it checks, if the user has a high difficulty this will almost always mean they find the best improvement (Steepest gradient). 
5. Returns most optimal leg

