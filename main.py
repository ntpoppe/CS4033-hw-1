from textbook_objects.problem import Problem
from textbook_objects.heuristics import hSLD_bucharest
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.greedy import greedy_best_first
from algorithms.a_star import astar

# testing the problems/algorithms should happen here
def main():
    problem1 = Problem(initial_state="Arad", goal="Bucharest")
    problem2 = Problem("Arad", "Oradea")

    bfs1_path = bfs(problem1)
    dfs1_path = dfs(problem1)
    greedy1_path = greedy_best_first(problem1, hSLD_bucharest)
    astar1_path = astar(problem1, hSLD_bucharest)

    bfs2_path = bfs(problem2)

    print(f"problem1 - BFS: {bfs1_path} - path cost: {problem1.path_cost(bfs1_path)}")
    print(f"problem1 - DFS: {dfs1_path} - path cost: {problem1.path_cost(dfs1_path)}")
    print(f"problem1 - greedy: {greedy1_path} - path cost: {problem1.path_cost(greedy1_path)}")
    print(f"problem1 - a*: {astar1_path} - path cost: {problem1.path_cost(astar1_path)}")

    print(f"problem2 - BFS: {bfs2_path} - path cost: {problem2.path_cost(bfs2_path)}")

if __name__ == "__main__":
    main()