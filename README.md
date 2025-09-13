### CS4033 - Homework 1
- The majority of the assignment has been split into different files.
- I attempted to follow the pseudo-code given by the textbook for the algorithms, hence the `Problem` class (`problem.py`). This class was used to determine the start and goal with helper functions.
- The Romania adjacency list is in `romania.py`. The SLD heuristic given by the textbook is in `heuristics.py`. I planned to have the other two heuristics implemented in the same file.
- Each search function is in it's own file as well:
    - `a_star.py`: A*
    - `bfs.py`: Breadth-First Search 
    - `dfs.py`: Depth-First Search
    - `greedy.py`: Greedy Best-First Search
- Each of these are imported into `main.py` to easily test. It holds examples of how to run each algorithm for different problems.