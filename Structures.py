class Queue:
    """
    A Queue class to be used in combination with state space
    search. The enqueue method adds new elements to the end. The
    dequeue method removes elements from the front.
    """
    def __init__(self):
        self.queue = []
    def __str__(self):
        result = "Queue contains " + str(len(self.queue)) + " items\n"
        for item in self.queue:
            result += str(item) + "\n"
        return result
    def enqueue(self, node):
        self.queue.append(node)
    def dequeue(self):
        if not self.empty():
            return self.queue.pop(0)
        else:
            raise Exception
    def size(self):
        return len(self.queue)
    def empty(self):
        return len(self.queue) == 0

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


class PriorityQueue:
    """
    Implements a heap-style priority queue with O(lg n) enqueue and
    dequeue methods.  The priority queue is stored as a list where
    position 0 always contains None.  The first actual item is stored
    in position 1.  This is necessary so that the list can be treated
    as a binary tree and simple calculations can be done to find the
    parent, and left and right sub-trees. The items being stored are
    expected to be instances of a class which has a priority() method.
    """
    def __init__(self):
        self.q = [None]
    def __str__(self):
        result = "Queue contains " + str(len(self.q)-1) + " items"
        if not self.empty():
            result += "-Minimum item has priority: " + \
                      str(self.min().priority())
        return result
    def parent(self, i):
        return int(i/2)
    def right(self, i):
        return (i * 2) + 1
    def left(self, i):
        return i * 2
    def hasLeft(self, i):
        return self.left(i) <= len(self.q)-1
    def hasRight(self, i):
        return self.right(i) <= len(self.q)-1
    def empty(self):
        return len(self.q) == 1
    def swap(self, p1, p2):
        self.q[p1], self.q[p2], = self.q[p2], self.q[p1]
    def bubbleUp(self,i):
        p = self.parent(i)
        if i==1 or self.q[i].priority() >= self.q[p].priority():
            return
        else:
            self.swap(i, p)
            self.bubbleUp(p)
    def bubbleDown(self, i):
        if (not self.hasLeft(i)) and (not self.hasRight(i)):
            return
        elif self.hasLeft(i) and (not self.hasRight(i)):
            l = self.left(i)
            if self.q[i].priority() > self.q[l].priority():
                self.swap(i, l)
                self.bubbleDown(l)
        else:
            l = self.left(i)
            r = self.right(i)
            key = self.q[i].priority()
            if self.q[l].priority() >= key and self.q[r].priority() >= key:
                return
            elif self.q[l].priority() <= self.q[r].priority():
                self.swap(i, l)
                self.bubbleDown(l)
            else:
                self.swap(i, r)
                self.bubbleDown(r)
    def min(self):
        if self.empty():
            raise RunTimeError
        return self.q[1]
    def dequeue(self):
        if self.empty():
            raise RunTimeError
        result = self.q.pop(1)
        self.q.insert(1, self.q.pop(len(self.q)-1))
        self.bubbleDown(1)
        return result
    def enqueue(self, item):
        self.q.append(item)
        self.bubbleUp(len(self.q)-1)
        
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
            print( current.state)
        print("Goal reached in", current.depth, "steps")
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
