from problem import Problem

class Node:
    def __init__(self, state, parent=None):
        self.state: str = state  # city (e.g. "Arad")
        self.parent: Node = parent

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
        self._q.sort(key=lambda x: x[0])  # lowest priority first

    def pop(self):
        if not self._q:
            return None
        return self._q.pop(0)[1]

def greedy_best_first(problem: Problem, heuristic: dict) -> list:
    root = Node(problem.initial_state)
    if problem.goal_test(root.state):
        return root.path() # if start is already the goal

    fringe = PriorityQueue() # priority queue ordered by h(n)
    fringe.push(heuristic[root.state], root)
    explored = {root.state} # mark start as explored

    while fringe:
        node = fringe.pop()
        if problem.goal_test(node.state):
            return node.path()

        for neighbor in problem.actions(node.state):
            if neighbor not in explored:
                child = Node(neighbor, node)
                if problem.goal_test(child.state):
                    return child.path()
                h = heuristic[root.state]
                fringe.push(h, child) # greedy: priority = h(n)
                explored.add(neighbor) # mark when added

    return []  # no path found
