"""
Rubix cube implementation
"""

class Rubix:
    """Implementation of nxm rubix cube - Only allows for 2 axis of rotation
    """    
    
    def __init__(self, i=2, j=2):
        """Initalizes a solved cube with i by j dimensions

        Args:
            i (int): number of rows
            j (int): number of columns
        """        
        pass
    
    def __init__(self,rowList, colList):
        """Initalizes a cube with preexisting values

        Args:
            rowList (string[]): ordered row value
            colList (string[]): ordered column values
        """
        pass
    
    def verifyCubeShape(rowList, colList):
        """Checks if cube shape is valid by doing modulus

        Args:
            rowList (string[]): ordered row value
            colList (string[]): ordered column values
        """        
        pass
    
    def possibleTurns(self):
        """Returns a list of all the supported moves
        """
        pass
    
    def isSolved(self):
        """Returns boolean whether the rubix cube has matching faces
        """
        pass
    
    def isSolvable(self):
        """Returns whether or not the cube is solvable
        """
        pass
    
    def turn(self, turnType):
        """Changes the state of the Rubix Cube 

        Args:
            turnType (String): A valid move from the possibleTurns list
        """        
        pass
    
    def turnX(self):
        """Turns the x plane - makes changes to just the row list
        """
        pass
    
    def turnY(self):
        """Turns the y plane - makes changes to both the row list and the column list
        """
        pass
    
    def scramble(self, x=5):
        """Scrambles a cube following a sequence of x moves

        Args:
            x (int): the number of random moves to be applied to the cube
        """        