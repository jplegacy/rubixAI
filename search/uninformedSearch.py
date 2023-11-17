class ProblemState:
    """
    An interface class for problem domains.  
    """
    def applyOperators(self):
        """
        Returns a list of legal successors to the current state.
        """
        abstract()
    def equals(self, state):
        """
        Tests whether the state instance equals the given state.
        """
        abstract()
    def dictkey(self):
        """
        Returns a string that can be used as a dictionary key to
        represent the unique state.
        """
        abstract()
        
class Node:
    """
    A Node class to be used in combination with state space search.  A
    node contains a state, a parent node, and the depth of the node in
    the search tree.  The root node should be at depth 0.
    """
    def __init__(self, state, parent, depth):
        self.state = state
        self.parent = parent
        self.depth = depth
    def __str__(self):
        result = "\nState: " +  str(self.state)
        result += "\nDepth: " + str(self.depth)
        if self.parent != None:
            result += "\nParent: " + str(self.parent.state)
        return result
class Search:
    """
    A general Search class that can be used for any problem domain.
    Given instances of an initial state and a goal state in the
    problem domain, this class will print the solution or a failure
    message.  The problem domain should be based on the ProblemState
    class.
    """
    def __init__(self, initialState, goalState, verbose=False):
        self.uniqueStates = {}
        self.uniqueStates[initialState.dictkey()] = True
        self.q = Queue()
        self.q.enqueue(Node(initialState, None, 0))
        self.goalState = goalState
        self.verbose = verbose
        solution = self.execute()
        if solution == None:
            print( "Search failed")
        else:
            self.showPath(solution)
    def execute(self):
        while not self.q.empty():
            current = self.q.dequeue()
            if self.goalState.equals(current.state):
                return current
            else:
                successors = current.state.applyOperators()
                for nextState in successors:
                    #if not self.uniqueStates.has_key(nextState.dictkey()):
                    # simple <key> in <dictionary> works too, but I find it 
                    # more semantically vague than 
                    # <key> in <dictionary>.keys()
                    if nextState.dictkey() not in self.uniqueStates.keys():
                        n = Node(nextState, current, current.depth+1)
                        self.q.enqueue(n)
                        self.uniqueStates[nextState.dictkey()] = True
                if self.verbose:
                    print( "Expanded:", current)
                    print( "Number of successors:", len(successors))
                    print("Queue length:", self.q.size())
                    print( "-------------------------------")
                
        return None
    def showPath(self, node):
        path = self.buildPath(node)        
        for current in path:
            print(current.state)
        print("Goal reached in", current.depth, "steps")

    def stringPath(self,node):
        path = self.buildPath(node)
        output = ""        
        for current in path:
            output += current.state.__str__()
        return output
            
    def buildPath(self, node):
        """
        Beginning at the goal node, follow the parent links back
        to the start state.  Create a list of the states traveled
        through during the search from start to finish.
        """
        result = []
        while node != None:
            result.insert(0, node)
            node = node.parent
        return result
