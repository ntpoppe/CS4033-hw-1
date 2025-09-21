from collections import deque
from textbook_objects.problem import Problem
from utils.counter import Counter

class Node:
    def __init__(self, state, parent=None):
        self.state: str = state # city (e.g. "Arad") 
        self.parent: Node = parent # city that connected to this city

    def path(self):
        node = self
        result = []

        while node:
            result.append(node.state)
            node = node.parent
        return list(reversed(result))

def dfs(problem: Problem, counter: Counter) -> list:
    root = Node(problem.initial_state)
    if problem.goal_test(root.state):
        return root.path() # if the goal is the start for some reason, return that "path"

    fringe = deque([root]) # initializes "queue" with root node
    explored = {root.state} # initializes explored set with root state

    while fringe:
        node = fringe.pop() # take from back
        counter.expanded += 1

        for neighbor in problem.actions(node.state):
            if neighbor not in explored:
                child = Node(neighbor, node) # wrap neighbor in a node to add to fringe
                if problem.goal_test(child.state):
                    return child.path()
                fringe.append(child)
                explored.add(neighbor)

    return [] # no path
