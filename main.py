from problem import Problem
from romania import romania_adj_list
from heuristics import hSLD_bucharest
from bfs import bfs
from dfs import dfs
from greedy import greedy_best_first
from a_star import astar

def main():
    problem1 = Problem(romania_adj_list, "Arad", "Bucharest")
    bfs1_path = bfs(problem1)
    dfs1_path = dfs(problem1)
    greedy1_path = greedy_best_first(problem1, hSLD_bucharest)
    astar1_path = astar(problem1, hSLD_bucharest)

    print(f"problem1 - BFS: {bfs1_path} - path cost: {problem1.path_cost(bfs1_path)}")
    print(f"problem1 - DFS: {dfs1_path} - path cost: {problem1.path_cost(dfs1_path)}")
    print(f"problem1 - greedy: {greedy1_path} - path cost: {problem1.path_cost(greedy1_path)}")
    print(f"problem1 - a*: {astar1_path} - path cost: {problem1.path_cost(astar1_path)}")

if __name__ == "__main__":
    main()