
class QueensPuzzle:
    
    """The aim of the application is to demonstrate all possible
    solutions for 8-Queens puzzle and print out the solutions in a form
    of 8-element array, each entry of which represents a column position of Q.
    Due to object oriented imlementation, it is possible to solve the puzzle
    for any N - number of Queens"""
    
    def __init__(self, chessboard):
        # Initializing the variables: counter of solutions and size of the board 
        # The chessboard size - will be given in the main class, 
        # This allows to use the code not only for 8 queens
        # but for any n - Queens
        self.solutions_counter = 0
        self.chessboard = chessboard
        # Running function findSolution() 
        self.findSolution()

        
    def checking_positions(self, current_positions, horizontal_const_met, vertical):
        # Checking vertical and 2 diagonal constraints
        # The horizontal constraint is given separately in another function
        
        for i in range(horizontal_const_met):
            if current_positions[i] == vertical or \
                current_positions[i] - i == vertical - horizontal_const_met or \
                current_positions[i] + i == vertical + horizontal_const_met:

                return False
        return True

        

    def place_queen(self, current_positions, next_row):
        # Function placing quens on possible place, which satisfies the constraints

        # If there are no next rows, base case is achived = no free rows to place
        if next_row == self.chessboard:
            self.show_solutions(current_positions)
            self.solutions_counter += 1
        else:
            for vertical in range(self.chessboard): 
                if self.checking_positions(current_positions, next_row, vertical):
                    current_positions[next_row] = vertical
                    self.place_queen(current_positions, next_row + 1)

        

    def findSolution(self):
        # Finding Solutions 
        current_positions = [-1] * self.chessboard
        self.place_queen(current_positions, 0)
        print("There are", self.solutions_counter, "possible solutions.")
        print("Each number represents the column position of a Queen for a specific solution.")



 
    def show_solutions(self, current_positions):
        # Displaying Solutions, Each number represents the position
        # in the column of an according row
 
        rows = ""
        for i in range(self.chessboard):
            rows += str(current_positions[i]) + " "
        print(rows)

def main():
    #Running the class QueenPuzzle
    QueensPuzzle(8)

if __name__ == "__main__":
    main()
