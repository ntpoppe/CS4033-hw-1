import heapq
from problem import Problem

class Node:
    def __init__(self, state, parent=None):
        self.state: str = state   # city (e.g. "Arad")
        self.parent: Node = parent

    def path(self):
        # reconstruct path from start to this node
        node, result = self, []
        while node:
            result.append(node.state)
            node = node.parent
        return list(reversed(result))

def greedy_best_first(problem: Problem, heuristic: dict) -> list:
    start = problem.initial_state
    root = Node(start)

    # if start is already the goal, return immediately
    if problem.goal_test(start):
        return root.path()
    
    fringe = [] # (min-heap, priority queue) ordered by h(n)
    heapq.heappush(fringe, (heuristic[start], root))

    explored = {start} # track visited states to avoid repeats

    # keep expanding until goal or frontier is empty
    while fringe:
        # pop node with smallest heuristic value
        _, node = heapq.heappop(fringe)

        # goal check
        if problem.goal_test(node.state):
            return node.path()

        # expand: generate all neighbors
        for nbr in problem.actions(node.state):
            if nbr not in explored:
                child = Node(nbr, node)

                # if child is the goal, return path right away
                if problem.goal_test(child.state):
                    return child.path()

                # push neighbor into frontier with priority = h(n)
                h = heuristic[nbr]
                heapq.heappush(fringe, (h, child))

                # mark as explored when added
                explored.add(nbr)

    # no path found
    return []
