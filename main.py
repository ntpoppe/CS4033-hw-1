import time
from typing import Callable
from statistics import mean
from textbook_objects.problem import Problem
from textbook_objects.heuristics import *
from textbook_objects.romania import romania_adj_list
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.greedy import greedy_best_first
from algorithms.a_star import astar
from utils.counter import Counter

# Runs an algorithm "repeats" times. The results (path) will 
# always be the same, so the repeats are just for a time comparison to other algorithms.
# Returns the last path, the last path cost, average expanded, and the total time to run n tests.
def time_runs(algorithm: Callable, *args):
    expanded_counts = []
    last_path = None

    # args[0] should always be a problem
    problem: Problem = args[0]

    start_time = time.time()
    for _ in range(100000):
        counter = Counter()
        last_path = algorithm(*args, counter=counter)
        expanded_counts.append(counter.expanded)
    total_time_ms = (time.time() - start_time) * 1000.0  # total in ms

    return {
        "path": last_path,
        "path_count": len(last_path),
        "path_cost": problem.path_cost(last_path),
        "avg_expanded": float(round(mean(expanded_counts))),
        "total_time_ms": round(total_time_ms, 3),
    }

def main():
    problem1 = Problem(initial_state="Arad", goal="Bucharest")
    problem2 = Problem("Arad", "Oradea")
    problem3 = Problem("Zerind", "Bucharest")

    print("\nEfficiency Tests\n")

    print("Problem 1: Arad to Bucharest")
    print("BFS:", time_runs(bfs, problem1))
    print("DFS:", time_runs(dfs, problem1))
    print("Greedy:", time_runs(greedy_best_first, problem1, hSLD_bucharest))
    print("A*:", time_runs(astar, problem1, hSLD_bucharest))

    print("\nProblem 2: Arad to Oradea") 
    heuristic1_v1 = heuristic1(problem2.goal, romania_adj_list)
    print("BFS:", time_runs(bfs, problem2))
    print("DFS:", time_runs(dfs, problem2))
    print("Greedy (triangle):", time_runs(greedy_best_first, problem2, heuristic1_v1))
    print("A* (triangle):", time_runs(astar, problem2, heuristic1_v1))

    print("\nProblem 3: Zerind to Bucharest") 
    heuristic1_v2 = heuristic1(problem3.goal, romania_adj_list)
    print("BFS:", time_runs(bfs, problem3))
    print("DFS:", time_runs(dfs, problem3))
    print("Greedy (triangle):", time_runs(greedy_best_first, problem3, heuristic1_v2))
    print("A* (triangle):", time_runs(astar, problem3, heuristic1_v2))

if __name__ == "__main__":
    main()