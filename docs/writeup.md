# Evaluation of Rubix AI

### Implementation and Design Choices of Rubix Cube
It turned out that implementing a Rubix Cube is a bit more challenging then it seems. From my proposal I assumed coming up with a heuristic function was going to be the hardest task of this project but arguably, it's on par with the implementation of the cube. The main questions behind the rubix's design choice was: 

- What's the easiest and most efficent structure for turning a side?
- How will movements be made?

In retrospect, implementating a graph to represent a cube could've been better to move around the data but settling on a dictionary of list storing each side with respect to a direction from a singular face was a pretty good choice. The benefits of this are that 


### Heuristic Functions

#### Heurisitc 1: Number of Colors per side 
    def heuristic(self):
        h = 0
        for  _, face in self.faces.items():
            numOfColors = len(np.unique(face))-1 
            if numOfColors== 4:
                h += 4
            elif numOfColors == 3:
                h += 2
            elif numOfColors == 2:
                h += 1

        return h

#### Heurisitc 2: Total of Pieces out of place
    def heuristic(self, goal):
        h = 0
        for  f, face in self.faces.items():
            h += np.sum(face != goal.faces[f])

        return h

#### Heurisitc 3: Total of Pieces out of place

    def heuristic(self):
        sum = 0
        face_count = 0
        for face in goal.faces:
            for block in face:
                if block != str(face_count):
                    sum += 1
            face_count += 1
        return sum

## Traversing Rubix Cube State Spaces with Informed Search Algorithms 