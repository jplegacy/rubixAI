import random
import numpy as np

from Astar import InformedProblemState

"""
Rubix Cube implementation

Similar implementation from https://github.com/soqt/Rubix-cube-Q-learning/blob/master/Cube.py#L78
"""

COLORS = {0: "O", 1: "R",2: "Y",3: "B",4: "G",5: "W"}

class Cube(InformedProblemState):
    """Implementation of nxn rubix - currently only has moves to solve 3x3 cubes 
    """    
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
        new = Cube(self.size)
        clonedFaces = {}
        for k,v in self.faces.items():
            clonedFaces[k] = np.copy(v)

        new.faces = clonedFaces
        return new                 
    
    def __str__(self):
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
        serial = ""
        for  _, face in self.faces.items():
            for row in face:
                serial+= "".join(row.tolist())
        return serial

    def dictkey(self):
        return self.__str__()

    def equals(self, otherCube):
        return self.serialize() == otherCube.serialize()

    def cw(self, face):
        side = self.faces[face]
        self.faces[face] = np.rot90(side, 3)
        connected = self.connectedEdges(face)
        
        temp = np.copy(connected[0])
        self.transferRow(connected[3], connected[0])
        self.transferRow(connected[2], connected[3])
        self.transferRow(connected[1], connected[2])
        self.transferRow(temp, connected[1])

    def cc(self,face):
        side = self.faces[face]
        self.faces[face] = np.rot90(side, 1)
        connected = self.connectedEdges(face)
        
        temp = np.copy(connected[3])
        self.transferRow(connected[0], connected[3])
        self.transferRow(connected[1], connected[0])
        self.transferRow(connected[2], connected[1])
        self.transferRow(temp, connected[2])
        
    def turn_180(self, face):
        self.cc(face)
        self.cc(face)

    def applyOperators(self):
        operations = []

        for move in self.MOVES:
            operations.append(self.produceNextTurn(move))

        return operations


    def transferRow(self, src, to):
        for i, src in enumerate(src):
            to[i] = src

    def connectedEdges(self, side):
        match side:
            # with respect to the current side, finds the neighboring pieces
            case 'f':
                left = self.faces['l'][:, self.size - 1] # uses np slicing to get last element from each row
                right = self.faces['r'][:, 0]
                up = self.faces['u'][self.size-1]
                bottom = self.faces['d'][0]
            
            case 'l':
                left = self.faces['b'][:, self.size - 1]
                up = self.faces['u'][:, 0]
                bottom = self.faces['d'][:, 0]
                right = self.faces['f'][:, 0]
            case 'b':
                left = self.faces['r'][:, self.size - 1]
                up = self.faces['u'][0]
                bottom = self.faces['d'][self.size -1]
                right = self.faces['l'][:, 0]
            case 'r':
                left = self.faces['f'][:, self.size - 1]
                up = self.faces['u'][:, self.size - 1]
                bottom = self.faces['d'][:, self.size-1]
                right = self.faces['b'][:, 0]
            case 'u':
                left = self.faces['l'][0]
                up = self.faces['b'][0]
                bottom = self.faces['f'][0]
                right = self.faces['r'][0]
            case 'd':
                left = self.faces['l'][self.size - 1]
                up = self.faces['f'][self.size - 1]
                bottom = self.faces['b'][self.size - 1]
                right = self.faces['r'][self.size - 1]
            case _:
                left = []
                right = []
                up = []
                bottom = []

        return (left, up, right, bottom)


    def produceNextTurn(self, action):
        clone = self.copy()

        if len(action) == 1:
            clone.cw(action)
        elif len(action) == 2:
            clone.cc(action[0])
        else: 
            clone.turn_180(action[0])
        
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
        for i in range(x):
            move = random.choice(self.possibleTurns())
            self.applyMove(move)
                
    def applySequence(self, seq):
        moves = seq.split()
        for move in moves:
            move = move.lower()
            self.applyMove(move)

    def applyMove(self, move):
        if len(move) == 1:
                self.cw(move)
        elif len(move) == 2:
            self.cc(move[0])
        else: 
            self.turn_180(move[0])

    def heuristic(self, goal):
        h = 0
        for  _, face in self.faces.items():
            numOfColors = len(np.unique(face))-1 # Each Side is supposed to have 1 color
            if numOfColors== 4:
                h += 4
            elif numOfColors == 3:
                h += 2
            elif numOfColors == 2:
                h += 1

        return h

    # def heuristic(self,goal):
    #     h = 0
    #     for  f, face in self.faces.items():
    #         h += np.sum(face != goal.faces[f])

    #     return h
        

    # def heuristic(self, goal):
    #     sum = 0
    #     face_count = 0
    #     for face in goal.faces:
    #         for block in face:
    #             if block != str(face_count):
    #                 sum += 1
    #         face_count += 1
    #     return sum

    

if __name__ == "__main__":
    r = Cube(3)
    r.turn_180("f")
    print(r)
    print("Solved?:", r.isSolved())