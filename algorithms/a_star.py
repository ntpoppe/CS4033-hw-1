from heapq import heappush, heappop
from textbook_objects.problem import Problem

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state: str = state # city (e.g. "Arad")
        self.parent: Node = parent # city that connected to this city
        self.g = g # path cost so far
        self.h = h # heuristic value

    def f(self):
        return self.g + self.h # evaluation function f(n) = g(n) + h(n)

    def path(self):
        node = self
        result = []
        while node:
            result.append(node.state)
            node = node.parent
        return list(reversed(result))

    # heappush needs something to compare on, so we can have node implement that.
    # this implements the comparison of two nodes by "less than".
    # lower f value == higher priority
    def __lt__(self, other):
        # compare nodes by f-value, break ties with g
        if self.f() == other.f():
            return self.g < other.g
        return self.f() < other.f()

def astar(problem: Problem, heuristic) -> list:
    start = problem.initial_state
    root = Node(start, None, 0, heuristic[start])

    # if start is already the goal, return immediately
    if problem.goal_test(start):
        return root.path()

    # frontier (min-heap, priority queue) of nodes to explore, ordered by f = g + h
    # each entry is a node
    fringe = []
    heappush(fringe, root)

    # best_g maps each state to the lowest g-value (cost so far) found for it
    # ensures we only expand the cheapest known path to any state
    best_g = {start: 0}

    # expand until frontier is empty or goal is found
    while fringe:
        # pop node with smallest f-value
        node = heappop(fringe)

        # if this entry is worse than the best known path, skip it
        if node.g != best_g.get(node.state, None):
            continue

        # if node is goal, reconstruct path from start → goal
        if problem.goal_test(node.state):
            return node.path()

        # expand: generate all successor states
        for nbr in problem.actions(node.state):
            # compute path cost to neighbor
            step = problem.step_cost(node.state, nbr)
            g_child = node.g + step

            # if this path is cheaper than any seen before for neighbor
            if g_child < best_g.get(nbr, float("inf")):
                best_g[nbr] = g_child # record improved cost

                # compute heuristic for neighbor
                h_child = heuristic[nbr]

                # build child node and push into frontier with new f
                child = Node(nbr, node, g_child, h_child)
                heappush(fringe, child)

    # if no path found, return empty list
    return []
