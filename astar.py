from Structures import *

class InformedNode(Node):
    def __init__(self, state, parent, depth, goalState):
        super().__init__(state, parent, depth)
        self.goalState = goalState

    def priority(self):
        return self.depth + self.state.heuristic(self.goalState)


class InformedSearch(Search):
    def __init__(self, initialState, goalState, verbose=False):
        self.uniqueStates = {}
        self.uniqueStates[initialState.dictkey()] = True
        self.q = PriorityQueue()
        self.q.enqueue(InformedNode(initialState, None, 0, goalState))
        self.goalState = goalState
        self.verbose = verbose
        self.nodeChecked = 0

        solution = self.execute()
        if solution == None:
            print("Search failed")
        else:
            # self.showPath(solution)
            print("Number of Expanded Nodes :", self.nodeChecked)
    def execute(self):
        while not self.q.empty():
            current = self.q.dequeue()
            self.nodeChecked += 1
            if self.goalState.equals(current.state):
                return current
            else:
                successors = current.state.applyOperators()
                for nextState in successors:
                    if nextState.dictkey() not in self.uniqueStates.keys():
                        n = InformedNode(nextState, current, current.depth+1, self.goalState)
                        self.q.enqueue(n)
                        self.uniqueStates[nextState.dictkey()] = True
                if self.verbose:
                    print( "Expanded:", current)
                    print( "Number of successors:", len(successors))
                    # print("Queue length:", self.q.size())
                    print( "-------------------------------")


