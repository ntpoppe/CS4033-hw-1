from problem import Problem

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

class PriorityQueue:
    def __init__(self):
        self._q = []

    def push(self, priority, item):
        self._q.append((priority, item))
        self._q.sort(key=lambda x: x[0]) # keep lowest priority first

    def pop(self):
        if not self._q:
            return None
        return self._q.pop(0)[1]

    def find_index_by_state(self, state):
        for i, (_, n) in enumerate(self._q):
            if n.state == state:
                return i
        return -1

    def priority_at(self, idx):
        return self._q[idx][0]

    def replace_at(self, idx, priority, item):
        self._q[idx] = (priority, item)
        self._q.sort(key=lambda x: x[0])

def astar(problem: Problem, heuristic) -> list:
    h0 = heuristic[problem.initial_state]
    root = Node(problem.initial_state, parent=None, g=0, h=h0)
    if problem.goal_test(root.state):
        return root.path()

    fringe = PriorityQueue() # ordered by f = g + h
    fringe.push(root.f(), root)
    explored = {root.state}

    while fringe:
        node = fringe.pop()
        if problem.goal_test(node.state):
            return node.path()

        # expand
        for neighbor in problem.actions(node.state):
            if neighbor in explored:
                continue

            # build child node with updated path cost g, heuristic h, and total f
            step = problem.step_cost(node.state, neighbor)
            g_child = node.g + step
            h_child = heuristic[neighbor]
            child = Node(neighbor, parent=node, g=g_child, h=h_child)
            f_child = child.f()

            # if neighbor is already in frontier with higher f, replace it, else insert
            idx = fringe.find_index_by_state(neighbor)
            if idx == -1:
                fringe.push(f_child, child)
            else:
                if f_child < fringe.priority_at(idx):
                    fringe.replace_at(idx, f_child, child)

    return [] # no path
