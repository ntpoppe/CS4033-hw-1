from problem import Problem
from heuristics import hSLD_bucharest
from bfs import bfs
from dfs import dfs
from greedy import greedy_best_first
from a_star import astar
from heuristics import *
from romania import romania_adj_list

# testing the problems/algorithms should happen here
def main():
    problem1 = Problem(initial_state="Arad", goal="Bucharest")
    problem2 = Problem("Arad", "Oradea")
    problem3 = Problem("Zerind", "Bucharest")

    bfs1_path = bfs(problem1)
    dfs1_path = dfs(problem1)
    greedy1_path = greedy_best_first(problem1, hSLD_bucharest)
    astar1_path = astar(problem1, hSLD_bucharest)

    bfs2_path = bfs(problem2)
    dfs2_path = dfs(problem2)
    heuristic1_h_value2 = heuristic1(problem2.goal, romania_adj_list)
    greedy2_path = greedy_best_first(problem2, heuristic1_h_value2)
    astar2_path = astar(problem2, heuristic1_h_value2)

    bfs3_path = bfs(problem3)
    dfs3_path = dfs(problem3)
    heuristic1_h_value3 = heuristic1(problem3.goal, romania_adj_list)
    greedy3_path = greedy_best_first(problem3, heuristic1_h_value3)
    astar3_path = astar(problem3, heuristic1_h_value3)

    print("\n--- Problem 1 ---\n")
    print(f"problem1 - BFS: {bfs1_path} - path cost: {problem1.path_cost(bfs1_path)}")
    print(f"problem1 - DFS: {dfs1_path} - path cost: {problem1.path_cost(dfs1_path)}")
    print(f"problem1 - greedy: {greedy1_path} - path cost: {problem1.path_cost(greedy1_path)}")
    print(f"problem1 - a*: {astar1_path} - path cost: {problem1.path_cost(astar1_path)}")

    print("\n--- Problem 2 ---\n")
    print(f"problem2 - BFS: {bfs2_path} - path cost: {problem2.path_cost(bfs2_path)}")
    print(f"problem2 - DFS: {dfs2_path} - path cost: {problem2.path_cost(dfs2_path)}")
    print(f"problem2 - greedy (triangle): {greedy2_path} - path cost: {problem2.path_cost(greedy2_path)}")
    print(f"problem2 - a* (triangle): {astar2_path} - path cost: {problem2.path_cost(astar2_path)}")

    print("\n--- Problem 3 ---\n")
    print(f"problem3 - BFS: {bfs3_path} - path cost: {problem3.path_cost(bfs3_path)}")
    print(f"problem3 - DFS: {dfs3_path} - path cost: {problem3.path_cost(dfs3_path)}")
    print(f"problem3 - greedy (triangle): {greedy3_path} - path cost: {problem3.path_cost(greedy3_path)}")
    print(f"problem3 - a* (triangle): {astar3_path} - path cost: {problem3.path_cost(astar3_path)}")

if __name__ == "__main__":
    main()