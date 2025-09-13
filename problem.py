from romania import romania_adj_list

# created this to mimic the pseudo-code from the book
# `main.py` has example of how it is used
class Problem():
    def __init__(self, initial_state, goal):
        self.graph = romania_adj_list # this should always be the romania adj. list
        self.initial_state = initial_state
        self.goal = goal

    def goal_test(self, state):
        return state == self.goal

    def actions(self, state):
        return list(self.graph[state].keys()) # returns neighbors of current state (city)

    def step_cost(self, state, action):
        return self.graph[state][action] # return cost (distnace) of a step

    # returns cost (distance) of entire path
    def path_cost(self, path):
        return sum(self.step_cost(path[i], path[i+1]) for i in range(len(path)-1))

    

        