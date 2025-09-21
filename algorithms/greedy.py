import heapq
from textbook_objects.problem import Problem
from utils.counter import Counter

class Node:
    def __init__(self, state, parent=None, h=0):
        self.state: str = state   # city (e.g. "Arad")
        self.parent: "Node" = parent
        self.h = h  # heuristic value for this node

    def path(self):
        # reconstruct path from start to this node
        node, result = self, []
        while node:
            result.append(node.state)
            node = node.parent
        return list(reversed(result))

    # heappush needs something to compare on, so we can have node implement that.
    # this implements the comparison of two nodes by "less than".
    # lower heuristic value == higher priority
    def __lt__(self, other):
        return self.h < other.h

def greedy_best_first(problem: Problem, heuristic: dict, counter: Counter) -> list:
    start = problem.initial_state
    root = Node(start, None, heuristic[start])

    # if start is already the goal, return immediately
    if problem.goal_test(start):
        return root.path()
    
    # frontier (min-heap, priority queue) of nodes, ordered by h(n)
    fringe = []
    heapq.heappush(fringe, root)

    explored = {start} # track visited states to avoid repeats

    # keep expanding until goal or frontier is empty
    while fringe:
        # pop node with smallest heuristic value
        node = heapq.heappop(fringe)
        counter.expanded += 1

        # goal check
        if problem.goal_test(node.state):
            return node.path()

        # expand: generate all neighbors
        for nbr in problem.actions(node.state):
            if nbr not in explored:
                child = Node(nbr, node, heuristic[nbr])

                # if child is the goal, return path right away
                if problem.goal_test(child.state):
                    return child.path()

                # push neighbor into frontier with priority = h(n)
                heapq.heappush(fringe, child)
                explored.add(nbr)

    # no path found
    return []

