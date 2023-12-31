"""
Author: Jeremy Perez
Date: November 2023

Rubix Cube nxn implementation using dictionaries and arrays.

Currently only has moves to solve 3x3 cubes but structurally supports nxn cubes

Similar implementation from https://github.com/soqt/Rubix-cube-Q-learning/blob/master/Cube.py#L78
"""

import random
import numpy as np

from search.astar import InformedProblemState


class Cube(InformedProblemState):
    COLORS = {0: "O", 1: "R",2: "Y",3: "B",4: "G",5: "W"}
    MOVES = ["f","b","r","l","u","d","f'","b'","r'","l'","u'","d'","f''","b''","r''","l''","u''","d''"]

    def __init__(self, size=3):
        self.size = size
        self.faces = {
            "f": np.full((size,size),0,dtype=str),
            "b" : np.full((size,size),1,dtype=str),
            "r": np.full((size,size),2,dtype=str),
            "l" : np.full((size,size),3,dtype=str),
            "u"   : np.full((size,size),4,dtype=str),
            "d" : np.full((size,size),5,dtype=str)
        }

    def copy(self):
        """Deep copies this cube 

        Returns:
            Cube: cloned copy of this cube
        """        
        new = Cube(self.size)
        clonedFaces = {}
        for k,v in self.faces.items():
            clonedFaces[k] = np.copy(v)

        new.faces = clonedFaces
        return new                 
    
    def __str__(self):
        """2D String representation of this cube using the following shape

          |u|
        |l|f|r|b|
          |d|

        where u:up, f:front, l:left, d:down, r:right, b:back

        Returns:
            String: 2D plot of all the faces of the cube

        2x2 Cube Example:
            3 3 
        0 0 1 1 2 2 4 4
        0 0 1 1 2 2 4 4
            5 5 
        """        
        output = ""
        blockSize = len(str(self.faces["f"][0]))
        for i in range(self.size):
            output += ' '*blockSize + str(self.faces["u"][i]) + '\n'
        for i in range(self.size):
            output += str(self.faces["l"][i]) + str(self.faces["f"][i]) +str(self.faces["r"][i]) + str(self.faces["b"][i]) + '\n'
        for i in range(self.size):
            output += ' '*blockSize + str(self.faces["d"][i]) + '\n'
        return output

    def serialize(self):
        """Reads out Cube in one line, where the index of string corresponds to it's reading using the following scheme

        2x2 Cube Example:
              0  1
              2  3  
        4  5  6  7  8  9  10 11
        12 13 14 15 16 17 18 19
              20 30
              31 32  
              

        Returns:
            String: Every Piece in sequence 
        """        
        serial = ""
        for  _, face in self.faces.items():
            for row in face:
                serial+= "".join(row.tolist())
        return serial


    def cw(self, face):
        """Applies 90 degree clockwise rotation on specified face

        Args:
            face (string): face name for rotation 
        """
        side = self.faces[face]
        self.faces[face] = np.rot90(side, 3)
        connected = self.connectedEdges(face)
        
        temp = np.copy(connected[0])
        self.transferRow(connected[3], connected[0])
        self.transferRow(connected[2], connected[3])
        self.transferRow(connected[1], connected[2])
        self.transferRow(temp, connected[1])

    def cc(self,face):
        """Applies 90 degree counter-clockwise rotation on specified face

        Args:
            face (string): face name for rotation 
        """        
        side = self.faces[face]
        self.faces[face] = np.rot90(side, 1)
        connected = self.connectedEdges(face)
        
        temp = np.copy(connected[3])
        self.transferRow(connected[0], connected[3])
        self.transferRow(connected[1], connected[0])
        self.transferRow(connected[2], connected[1])
        self.transferRow(temp, connected[2])
        
    def turn_180(self, face):
        """Applies 180 degree rotation on specified face

        Args:
            face (string): face name for rotation 
        """
        self.cc(face)
        self.cc(face)
    
    def transferRow(self, src, to):
        """Swaps values in the cube from a specified location 

        Args:
            src (np.array): original value locations
            to (np.array): new values replacing old
        """        
        for i, src in enumerate(src):
            to[i] = src

    def connectedEdges(self, side):
        """Finds edges correponding(touching) a specified side 

        Args:
            side (string): Name of the side in question

        Returns:
            tuple: 4 tuple of all the rows using the following structure (left, up, right, bottom)
        """        
        # with respect to the current side, finds the neighboring pieces
        if side == 'f':
            left = self.faces['l'][:, self.size - 1] # uses np slicing to get last element from each row
            right = self.faces['r'][:, 0]
            up = self.faces['u'][self.size-1]
            bottom = self.faces['d'][0]
        
        elif side == 'l':
            left = self.faces['b'][:, self.size - 1]
            up = self.faces['u'][:, 0]
            bottom = self.faces['d'][:, 0]
            right = self.faces['f'][:, 0]
        elif side == 'b':
            left = self.faces['r'][:, self.size - 1]
            up = self.faces['u'][0]
            bottom = self.faces['d'][self.size -1]
            right = self.faces['l'][:, 0]
        elif side == 'r':
            left = self.faces['f'][:, self.size - 1]
            up = self.faces['u'][:, self.size - 1]
            bottom = self.faces['d'][:, self.size-1]
            right = self.faces['b'][:, 0]
        elif side == 'u':
            left = self.faces['l'][0]
            up = self.faces['b'][0]
            bottom = self.faces['f'][0]
            right = self.faces['r'][0]
        elif side == 'd':
            left = self.faces['l'][self.size - 1]
            up = self.faces['f'][self.size - 1]
            bottom = self.faces['b'][self.size - 1]
            right = self.faces['r'][self.size - 1]
        else:
            left = []
            right = []
            up = []
            bottom = []

        return (left, up, right, bottom)


    def produceNextTurn(self, move):
        """Given a move produces a cloned Cube with the new move applied

        Args:
            move (String): Move getting applied to new cube

        Returns:
            Cube: New Cube
        """        
        clone = self.copy()

        if len(move) == 1:
            clone.cw(move)
        elif len(move) == 2:
            clone.cc(move[0])
        else: 
            clone.turn_180(move[0])
        
        return clone
                    
    def possibleTurns(self):
        """Returns a list of all the supported moves
        """
        return self.MOVES
    
    def isSolved(self):
        """Returns boolean whether the rubix cube has matching faces
        """
        for  _, face in self.faces.items():
            element = face[0][0]
            solved = np.all(face == element)
            if not solved:
                return False
        return True
    
    def scramble(self, x=5):
        """Scrambles a cube following a sequence of x moves

        Args:
            x (int): the number of random moves to be applied to the cube
        """ 
        sequence = ""   
        for i in range(x):
            move = random.choice(self.possibleTurns())
            sequence += move + " "
            self.applyMove(move)
        return sequence
            
                
    def applySequence(self, seq):
        """Applies a sequence of moves on this cube

        Args:
            seq (String): Sequence of whitespace seperated valid moves 
        """        
        moves = seq.split()
        for move in moves:
            assert move in self.MOVES
            
            move = move.lower()
            self.applyMove(move)

    def applyMove(self, move):
        if len(move) == 1:
                self.cw(move)
        elif len(move) == 2:
            self.cc(move[0])
        else: 
            self.turn_180(move[0])

    #----------------------------------------------------------------
    # REQUIRED METHODS TO IMPLEMENT InformedProblemState
    #----------------------------------------------------------------


    def applyOperators(self):
        """Produces a list of all possible cubes that can be produced from this given cube.

        Returns:
            Cube[]: list of cubes that can be produced using 1 move from MOVES constant
        """        
        operations = []

        for move in self.MOVES:
            operations.append(self.produceNextTurn(move))

        return operations


    def dictkey(self):
        """Produces a unique identifier for this given state
        """

        #TODO: Can be improved to encapcilate permuation and other symmetries
        return self.serialize()

    def equals(self, otherCube):
        """Compares two cube's and returns whether or not both cube's are the same
        """        

        #TODO: Can be improved to pick up on symmetric permuations of a rubix cube
        return self.serialize() == otherCube.serialize()

    def heuristic(self, goal):
        """Heuristic Function that calculates how 

        Args:
            goal(Cube): state that this heuristic is being calculated on

        Returns:
            int: the number of collective extra colors on each side of the cube
        """        
        
        h = 0
        for  _, face in self.faces.items():
            numOfColors = len(np.unique(face))-1
            if numOfColors== 4:
                h += 4
            elif numOfColors == 3:
                h += 2
            elif numOfColors == 2:
                h += 1
            # Each Side is supposed to have 1 color so technically h+=0 proceeds

        return h

if __name__ == "__main__":
    r = Cube(3)
    r.turn_180("f")
    print(r)
    print("Solved?:", r.isSolved())